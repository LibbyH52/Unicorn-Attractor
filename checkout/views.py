from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from features.models import Feature
import stripe


stripe.api_key = settings.STRIPE_SECRET



@login_required
def checkout(request):
	order_form = OrderForm()
	payment_form = MakePaymentForm()
	if request.method == "POST":
		order_form = OrderForm(request.POST)
		payment_form = MakePaymentForm(request.POST)
		if order_form.is_valid and payment_form.is_valid():
			order = order_form.save(commit=False)
			order.date = timezone.now()
			order.save()
			for id, qunatity in cart.items():
				feature = get_object_or_404(Feature, pk=id)
				total += quantity * feature.vote_price
				order_line_item = OrderLineItem(
				order=order,
				feature=feature,
				quantity=quantity
				)
				order_line-item.save()
			try:
				charge = stripe.Charge.create(
				amount = int(total*100),
				currency = "EUR",
				description = request.user.email,
				card = payment_form.cleaned_data['stripe_id']
				)
			except stripe.error.CardError:
				messages.error(request, "Your card was declined!")
			if charge.paid:
				messages.success(request, "You have successfully paid!")
				request.session['cart'] = {}
				feature.upvote += quantity
				return redirect(reverse('get_features'))
			else:
				messages.error(request, "Unable to take payment!")
		else:
			print(payment_form.errors)
			messages.error(request, "We were unable to take payment with that card!")
	else:
		payment_form = MakePaymentForm()
		order_form = OrderForm()
	return render(request, 'checkout/checkout.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
