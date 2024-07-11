from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import auth
from .forms import *

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'main/home.html')
    
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'main/register.html', {'form': form, 'error':"Такое имя уже есть!"})
    else:
        form = RegisterForm()

    return render(request, 'main/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username = username, password = password)
            if user is None:
                return render(request, 'main/login.html', {'form': form, 'error':"Вы ввели чтото не правильно!"})
            else:
                auth.login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form})