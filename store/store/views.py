from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request,'index.html', {
        'message' : 'Product list', 
        'title': 'Products',
        'products': [
            {
                'title': 'T-shirt', 
                'prince':5, 
                'stock': True
            },
            {
                'title': 'Bag', 
                'prince':2, 
                'stock': True
            },
            {
                'title': 'Pants', 
                'prince':10, 
                'stock': False
            }         
        ]
    })

def login_view(request):
    print(request.method)
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