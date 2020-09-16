from django.contrib import admin

# Register your models here.
from .models import Product

# Se modifica que campos se puede ver en el administrador
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'price')
    list_display = ('__str__', 'slug', 'created_at')

# admin.site.register(Product)
admin.site.register(Product, ProductAdmin)

