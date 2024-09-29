from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required

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


@login_required(redirect_field_name='login_user')
def profile(request):
    return render(request, 'users/profile.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(user)
            messages.success(request, 'Login Successful')
            return redirect('profile')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login_user')
    return render(request, 'users/login_user.html')


@login_required(redirect_field_name='login_user')
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successfully.')
            return redirect('profile')
    form = CustomUserChangeForm(instance= request.user)
    return render(request, 'users/edit_profile.html', {'form': form})
