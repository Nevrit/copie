from . import views
from django.urls import path

urlpatterns = [
    path('cart/checkout/', views.checkout, name='checkout-pay'),
    path('cart/checkout/payment-done', views.payment_done, name='congratulation'),
]