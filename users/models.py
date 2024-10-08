
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from base.models import BaseModel

# Create your models here.
class  CustomUser(BaseModel, AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=False, blank=False)
    contact = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=200)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact', 'address']

    objects = UserManager()

    def __str__(self) -> str:
        return f"self.email"
