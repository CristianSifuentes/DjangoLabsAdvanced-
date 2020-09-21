from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name="productsearch_view"),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_view' )
]
