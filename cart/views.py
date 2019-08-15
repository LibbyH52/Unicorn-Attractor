from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """
    Displays items in a schopping cart
    """
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
    return render(request, 'cart/cart.html', {'cart': cart})

def adjust_cart(request, id):
    """
    A view to allow the user to increase / decrease the 
    number of upvotes for a particular feature.
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(str(id))
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
