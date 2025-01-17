from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Advertisement
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import signupform, AdvertisementForm
from django.contrib.auth.decorators import login_required

def helloworld(request):
    all_products = Product.objects.all()
    all_advertisements = Advertisement.objects.all()  # دریافت همه‌ی آگهی‌ها
    return render(request, 'index.html', {
        'products': all_products,
        'advertisements': all_advertisements  # ارسال آگهی‌ها به تمپلیت
    })

def about(request):
    return render(request, "about.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("با موفقیت وارد شدید"))
            return redirect('home')
        else:
            messages.success(request, ("رمز یا نام کاربری اشتباه است"))
            return redirect('login')
    else:
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.success(request, ('با موفقیت خارج شدید'))
    return redirect('/')

def signup_user(request):
    form = signupform()
    if request.method == "POST":
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, "اکانت شما با موفقیت ساخته شد")
                return redirect('home')
        else:
            messages.error(request, "مشکلی در ثبت نام شما وجود دارد")
    return render(request, 'signup.html', {"form": form})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def advertisement_detail(request, pk):
    advertisement = get_object_or_404(Advertisement, id=pk)
    return render(request, 'advertisement_detail.html', {'advertisement': advertisement})

def category(request, cat):
    cat = cat.replace('-', ' ')
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, ("دسته بندی وجود ندارد!"))
        return redirect("home")

@login_required
def add_advertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)  # request.FILES برای آپلود عکس
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = request.user  # کاربر فعلی رو به آگهی لینک کن
            advertisement.save()
            messages.success(request, "آگهی شما با موفقیت اضافه شد!")  # پیام موفقیت
            return redirect('home')  # بعد از اضافه کردن، به صفحه‌ی اصلی برو
        else:
            messages.error(request, "مشکلی در اضافه کردن آگهی وجود دارد!")  # پیام خطا
    else:
        form = AdvertisementForm()
    return render(request, 'add_advertisement.html', {'form': form})