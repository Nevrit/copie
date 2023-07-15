from . import views
from django.urls import path

urlpatterns = [
    path('product/<slug:slug>/add-to-cart', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),
    path('cart_delete/', views.cart_delete, name='cart-delete'),
    path('cart_article_delete/<slug:slug>/', views.cart_article_delete, name="cart-article-delete"),
    # path('cart/checkout', views.checkout, name='checkout'),
]