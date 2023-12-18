from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
import os
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def homepage(request):
    return render(request, 'elevate/index.html')

def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect("login") 
    
    context = {'registerform':form}
    
    
    return render(request, 'elevate/register.html', context = context)

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, passwors = password)
            
            if user is not None:
                authenticate.login(request, user)
                
            return redirect("dashboard")
            
    context = {'loginform': form}
    
    return render(request, 'elevate/login.html', context = context)


def user_logout(request):
    authenticate.logout(request)
    return redirect("index")
    

@login_required(login_url="login")
def dashboard(request):
    return render(request, 'elevate/dashboard.html')