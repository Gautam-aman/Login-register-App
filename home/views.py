from django.shortcuts import render, redirect
from django.http import HttpRequest , HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def Home(request):
    if request.method=="POST":
        data= request.POST
        username= data.get('username')
        password= data.get('password')
        
        user = User.objects.all()
        if not User.objects.filter(username= username):
            messages.warning(request, 'Invalid username')
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request,'Inavlid credentials')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/home/')
        
        
        
    return render(request, 'login.html')

def home_page(request):
    return render (request, 'home.html')

def Register(request):
    if request.method=="POST":
        data= request.POST
        username=data.get('username')
        password=data.get('password')
        
        user =User.objects.filter(username=username)
        if user.exists():
            messages.error(request, 'Username already exist')
            return redirect('/register/')
        else:
            user=User.objects.create(
                username=username
            )
            user.set_password(password)
            user.save()
            messages.info(request, 'Account Created successfully')
            return redirect('/login/')
        
    return render(request , 'register.html')


    
