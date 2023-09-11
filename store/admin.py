from django.contrib import admin
from store.models import Cart, Category, Galery, Order, Product


# Register your models here.
class GaleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image',]
    search_fields = ['title']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_quantity', 'image']
    search_fields = ['name']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'ordered']
    search_fields = ['user', 'product']
    
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user', 'orders']
    
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Galery, GaleryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
