from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.all()
    items_images = []
    
    # Prepare a list of products with their first image
    for product in products:
        first_image = product.product_image.first()  # Get the first image for each product
        items_images.append({'product': product, 'first_image': first_image})
    
    return render(request, 'products/products.html', {'items_images': items_images})


def product(request, product_slug):
    product = Product.objects.get(product_slug=product_slug)
    return render(request, 'products/product.html', {'product' : product})