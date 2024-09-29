from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .models import CustomUser

# Create your views here.
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if CustomUser.objects.filter(email = email).exists():
            messages.info(request, 'User already exists with this email.')
            return redirect('register')
        if request.POST.get('contact') is None:
            messages.info(request, 'contact info is required')
            return redirect('register')
        if request.POST.get('address') is None:
            messages.info(request, 'address is required')
            return redirect('register')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/')
        else:
            messages.error(request, 'There was an error in your form submission.')

    form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})