from django.shortcuts import render, redirect, reverse


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, id):
    """
    Allows a user to upvote a feature by
    adding it to their cart
    """
    quantity = 1
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    print(cart)
    return redirect(reverse('get_features'))
