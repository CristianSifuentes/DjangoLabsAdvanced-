from django.shortcuts import render
from django.views.generic.list import ListView
from products.models import Product

# Create your views here.
class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Product list'
        context['products'] = context['product_list']
        print(context)
        return context
