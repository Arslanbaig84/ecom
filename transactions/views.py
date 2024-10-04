from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url="/users/login_user/")
def add_to_cart(request, product_slug):
    # Get the current user
    user = request.user

    # Fetch the product based on slug
    product = get_object_or_404(Product, product_slug=product_slug)

    # Check if the user already has an active cart, create one if not
    cart, created = Cart.objects.get_or_create(user=user, is_active=True)

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if created:
        cart_item.save()
        messages.success(request, 'Product added to cart.')
    else:
        messages.info(request, 'Product already in cart.')

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url="/users/login_user/")
def cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'transactions/cart.html', {'cart':cart})