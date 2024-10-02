from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<product_slug>', views.product, name='product')
]