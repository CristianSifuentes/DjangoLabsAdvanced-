from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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
            return redirect('index')
        else:
            print('user no authenticated')

    return render(request, 'users/login.html', {})