# z_app views
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from .models import UserProfile



# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def profiles(request):
    if request.user.is_authenticated:
        profile_list = UserProfile.objects.exclude(user=request.user)
        return render(request, 'profiles.html', {"Profiles":profile_list})
    else:
        messages.success(request,"Please create an account to view this page or login if you have an existing account with us.")
        return redirect('home')

def profile(request,pk):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user_id=pk)
        return render(request, 'profile.html',{"profile":profile})
    else:
        messages.success(request,"Please create an account to view this page or login if you have an existing account with us.")
        return redirect('home')
    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Successful login.")
            return redirect('home')
        else:
            messages.success(request,"Login failed.")
            return redirect('login')
    else:
        return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"User logged out.")
    return redirect('login')

def register_newuser(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Successfully created an account.")
            return redirect('home')
        
    return render(request, 'register.html', {'form':form})