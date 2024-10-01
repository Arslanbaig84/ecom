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
