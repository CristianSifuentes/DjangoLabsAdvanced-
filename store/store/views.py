from django.http import HttpResponse
from django.shortcuts import render

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