
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile')
]
