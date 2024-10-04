from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<slug:product_slug>', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('order', views.order, name='order')
]