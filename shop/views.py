from django.shortcuts import render , redirect 
from . models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import signupform



def helloworld(request):
  all_products = Product.objects.all()
  return render(request , 'index.html',{'products': all_products})


def about(request):
  return render(request , "about.html")

def login_user(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request , username=username ,password=password)
    if user is not None:
      login(request , user)
      messages.success(request, ("با موفقیت وارد شدید"))
      return redirect('home')
    else:  
      messages.success(request, ("رمز یا نام کاربری اشتباه است"))
      return redirect('login')
  else:  
    return render(request, "login.html")

def logout_user(request):
  logout(request)
  messages.success(request , ('با موفقیت خارج شدید'))
  return redirect('/')


def signup_user(request):
  form = signupform()
  if request.method == "POST":
    form = signupform(request.POST)
    if form.is_valid:
      form.save()
      username = form.cleaned_data['username']
      password1 = form.cleaned_data['password1']
      user = authenticate(request , username=username ,password=password1)
      login(request , user)
      messages.success(request, ("اکانت شما با موفقیت ساخته شد"))
      return redirect('home')
    else:
      messages.success(request, ("مشکلی در ثبت نام شما وجود دارد"))
      return redirect('home')
  return render(request , 'signup.html' , {"form" : form})