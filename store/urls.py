from . import views
from django.urls import path

urlpatterns = [
    path('product/<slug:slug>/add-to-cart', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),
]