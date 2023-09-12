from ipaddress import summarize_address_range
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.utils import timezone

from store.models import Cart, Order, OrderOrder, OrderedItem


# Create your views here.

def checkout(request):
    cart_user = get_object_or_404(Cart, user=request.user)
    items = cart_user.orders.all()
    paniers = Order.objects.filter(user=request.user)
    total_price = 0

    for item in items:
        total_price += item.product.price * item.quantity

    context = {'cart_user': cart_user, 'items': items, 'total_price': total_price,}

    if request.method == 'POST':
        # Récupérer les données de la requête POST
        lastname = request.POST.get('nom')
        firstname = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        another_phone = request.POST.get('autre_telephone')
        city = request.POST.get('ville')
        delivery_address = request.POST.get('adresse')
        payment_method = request.POST.get('payment_method')

        # Créer une nouvelle commande conformément au modèle OrderOrder
        order = OrderOrder.objects.create(
            user=request.user,
            lastname=lastname,
            firstname=firstname,
            telephone=telephone,
            another_phone=another_phone,
            city=city,
            delivery_address=delivery_address,
            payment_method=payment_method,
            # total=total_price,
            ordered_date=timezone.now()
        )

        # Récupération des éléments du panier
        for item in items:
            order_item = OrderedItem()
            order_item.product = item.product
            order_item.order_id = order
            order_item.user = request.user
            order_item.price = item.product.price
            order_item.quantity = item.quantity
            order_item.total = item.quantity * item.product.price

            order_item.save()
        # Récupération des éléments du panier
        paniers.delete()
        # Rediriger l'utilisateur vers une autre page après le traitement réussi
        return redirect(payment_done)

    return render(request, 'home/pay/checkout.html', context)


def payment_done(request):
    return render(request, 'home/pay/congrat.html')
