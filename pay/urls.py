from . import views
from django.urls import path

urlpatterns = [
    path('cart/checkout/', views.checkout, name='checkout-pay'),
]