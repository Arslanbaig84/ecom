from django.db import models
from base.models import BaseModel
from users.models import CustomUser
from products.models import Product

# Create your models here.
class Cart(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart')
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'cart of self.user.email'

    def total_price(self):
        return sum(item.price() for item in self.cart_items.all())    

class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')

    def __str__(self) -> str:
        return f"self.product.product_name"
    
    def price(self):
        return self.product.product_price
