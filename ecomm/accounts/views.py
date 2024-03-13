from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import *



def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = email)

        if not user.exists():
            messages.warning(request , "Account not found")
            return redirect('login')
        
        if not user[0].profile.is_verified:
            messages.warning(request, "Your email is not verified! Verify First")
            return redirect('login')
        
        user = authenticate(username = email, password=password)
        if user:
            login(request , user)
            return redirect("/")
       
        messages.warning(request, "Invalid Credentials")
        
        return redirect('register')
    
    return render(request, 'accounts/login.html')



def register_page(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = email)

        if user.exists():
            messages.warning(request, "Email is already registered! Log in below.")
            return redirect('register')
        
        user=User.objects.create(first_name=first_name, last_name=last_name, email=email, username = email)
        user.set_password(password)
        user.save()
       
        messages.success(request, "Code Has been send to your mail!")
        return redirect('register')
         
    return render(request, 'accounts/register.html')


def activate_email(request, email_token):
    try:
        user= Profile.objects.get(email_token = email_token)
        user.is_verified=True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email Token')
