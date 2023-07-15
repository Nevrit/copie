from ipaddress import summarize_address_range
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from store.models import Cart,Order

# Create your views here.

def checkout(request):
    cart_user = get_object_or_404(Cart, user=request.user)
    items = cart_user.orders.all()
    
    # commande = Order.objects.filter(user=request.user)
    total_price = 0
    for item in items:
        total_price += item.product.price * item.quantity
        
    context = {'cart_user' : cart_user, 'items':items, 'total_price' : total_price}

    
    return render(request, 'home/pay/checkout.html', context)

