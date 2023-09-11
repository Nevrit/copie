from ipaddress import summarize_address_range
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.utils import timezone
from store.models import Cart,Order

# Create your views here.

def checkout(request):
    cart_user = get_object_or_404(Cart, user=request.user)
    items = cart_user.orders.all()
    total_price = 0
    for item in items:
        total_price += item.product.price * item.quantity

    context = {'cart_user': cart_user, 'items': items, 'total_price': total_price}

    if request.method == 'POST':
        # Récupérer la date du jour
        ordered_date = timezone.now()

        # Mettre à jour chaque article du panier pour indiquer qu'il a été commandé
        for item in items:
            item.ordered = True
            item.ordered_date = ordered_date
            item.save()

        # Réinitialiser le panier en retirant tous les articles
        cart_user.orders.clear()
        cart_user.ordered = False
        cart_user.ordered_date = None
        cart_user.save()

        # Rediriger l'utilisateur vers une autre page après le traitement réussi
        return redirect(payment_done)
    else:
        print('Nevrit')

    return render(request, 'home/pay/checkout.html', context)


def payment_done(request):
    return render(request, 'home/pay/congrat.html')

