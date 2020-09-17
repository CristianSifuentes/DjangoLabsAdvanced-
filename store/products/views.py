from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from products.models import Product

# Create your views here.
class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Product list'
        context['products'] = context['product_list']
        # print(context['products'])
        return context

class ProductDetailView(DetailView):#id -> pk
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context


class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.query())
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()
        # print(context['products'])
        return context

