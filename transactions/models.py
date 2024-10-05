from django.db import models
from base.models import BaseModel
from users.models import CustomUser
from products.models import Product

# Create your models here.
class Cart(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart')
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'is_active')

    def __str__(self) -> str:
        return f'cart of self.user.email'


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')

    def __str__(self) -> str:
        return f'self.product.product_name'
    
    def price(self):
        return self.product.product_price


# Order and OrderItem
class Order(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('shipped', 'Shipped')], default='pending')

    def __str__(self) -> str:
        return f'Order by {self.user.email}'

    def total_price(self):
        return sum(item.price() for item in self.order_items.all())


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ordered_products')
    quantity = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return self.product.product_name

    def price(self):
        return self.quantity * self.product.product_price