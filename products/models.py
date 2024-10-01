from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

# Create your models here.
class Category(BaseModel):
    category_name = models.CharField(max_length=200)
    category_slug = models.SlugField(unique=True, null=True, blank=True)
    category_description = models.TextField(max_length=500)

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name
    

class Product(BaseModel):
    product_name = models.CharField(max_length=200)
    product_slug = models.SlugField(unique=True, null=True, blank=True)
    product_categoty = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    product_price = models.PositiveIntegerField()
    product_desctiption = models.TextField(max_length=500)

    def save(self, *args, **kwargs):
        self.product_slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name
    

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='products/images')