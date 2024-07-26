from django.contrib import admin
from store.models import Cart, Category, Galery, Order, Product, OrderOrder, OrderedItem, WhishListItem, WishList


# Register your models here.
class GaleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', ]
    search_fields = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_quantity', 'image']
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name']


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['user', 'product', 'quantity', 'ordered']
#     search_fields = ['user', 'product']

class CartAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user', 'orders']
    
class WishListAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user', 'products']


class OrderOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'lastname', 'firstname', 'telephone', 'another_phone', 'city', 'delivery_address',
                    'payment_method']
    search_fields = ['user', 'lastname', 'firstname', 'telephone', 'another_phone', 'city', 'delivery_address',
                     'payment_method']


class OrderedItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'order_id', 'quantity', 'price', 'total']
    search_fields = ['user', 'product', 'order_id', 'quantity', 'price', 'total']
    
class WhishListItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
    search_fields = ['user', 'product']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Galery, GaleryAdmin)
# admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(OrderOrder, OrderOrderAdmin)
admin.site.register(OrderedItem, OrderedItemAdmin)
admin.site.register(WishList ,WishListAdmin)
admin.site.register(WhishListItem, WhishListItemAdmin)
