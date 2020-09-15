from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from products.models import Product

def index(request):
    
    products = Product.objects.all().order_by('-id')

    return render(request,'index.html', {
        'message' : 'Product list',
        'title': 'Products',
        'products': products
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    # print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username') #diccionary
        password = request.POST.get('password')
        print(username)
        print(password)

        user = authenticate(username=username, password=password) #none
        if user:
            login(request, user)
            print('user authenticated')
            messages.success(request, 'Welcome {}'.format(user.username))
            return redirect('index')
        else:
            print('user no authenticated')
            messages.error(request, 'User invalid')


    return render(request, 'users/login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'Session closed successfully')
    return redirect('login_view')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('login_view')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        #  username = form.cleaned_data.get('username')
        #  email = form.cleaned_data.get('email')
        #  password = form.cleaned_data.get('password')

        #  user = User.objects.create_user(username, email, password)
         user = form.save()
         if user:
             login(request, user)
             messages.success(request, 'User created successfully')
             return redirect('index')

    return render(request,'users/register.html', {
          'form': form
    })