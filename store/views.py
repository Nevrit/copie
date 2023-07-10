from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from store.models import Cart, Order, Product
from django.contrib import messages
from django.shortcuts import redirect
from Home.views import index 

# Création des informations du panier
def add_to_cart(request, slug):
    user = request.user # On récupère les informations du client
    product = get_object_or_404(Product, slug=slug) # On récupère le slug du produit s'il existe sinon on lève une erreur
    cart, _ = Cart.objects.get_or_create(user=user) # On récupère le panier de l'utilisateur s'il existe sinon on le crée
    order, created = Order.objects.get_or_create(user=user, ordered = False, product=product) # On récupère la commande de l'utilisateur s'il existe sinon on le crée
    
    # Si la commande n'existe pas, on la créée et on ajoute la commande sélectionnée
    if created:
        cart.orders.add(order)
        cart.save()
    # Si la commande n'existe pas, on la créée et on ajoute la commande sélectionnée
    
    # Si la commande existe déjà, on incrémente la quantité 
    else:
        order.quantity +=1
        order.save()
    # Si la commande existe déjà, on incrémente la quantité 
    
    return HttpResponseRedirect(reverse("products_description", kwargs={'slug' : slug}))

# Gestion du panier
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'home/page/cart.html', context={"orders" : cart.orders.all()})


def cart_delete(request):
    cart = request.user.cart
    if cart:
        # cart.orders.all().delete()
        cart.delete()
        # messages.success(request, "L'élément a été supprimé du panier.")
    return redirect(index)

def cart_article_delete(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart = get_object_or_404(Cart, user=user, orders__product=product)
    order = get_object_or_404(Order, user=user, product=product)
    
    if order.quantity > 1:
        order.quantity -= 1
        order.save()
    else:
        cart.orders.remove(order)
        order.delete()
    
    messages.success(request, "L'article a été supprimé du panier.")
    # return HttpResponseRedirect(reverse("cart"))
    return HttpResponseRedirect(reverse("products_description", kwargs={'slug' : slug}))

