from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone
from .forms import MakePaymentForm
from features.models import Feature
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
	if request.method == "POST":
		payment_form = MakePaymentForm(request.POST)
		if payment_form.is_valid():
			cart = request.session.get('cart', {})
			total = 0
			for id, quantity in cart.items():
				feature = get_object_or_404(Feature, pk=id)
				feature.upvote += quantity
				total += quantity * feature.vote_price
			try:
				charge = stripe.Charge.create(
				amount = int(total * 100),
				currency = "EUR",
				description = request.user.email,
				card = payment_form.cleaned_data['stripe_id']
				)
			except stripe.error.CardError:
				messages.error(request, "Your card was declined!")
			if charge.paid:
				messages.success(request, "You have successfully paid!")
				request.session['cart'] = {}
				return redirect(reverse('get_features'))
			else:
				messages.error(request, "Unable to take payment!")
		else:
			print(payment_form.errors)
			messages.error(request, "We were unable to take payment with that card!")
	else:
		payment_form = MakePaymentForm()
	return render(request, 'checkout/checkout.html', {'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})