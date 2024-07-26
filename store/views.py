from django.http import HttpResponseRedirect # type: ignore
from django.shortcuts import get_object_or_404, render # type: ignore
from django.urls import reverse # type: ignore
from store.models import Cart, Order, Product, WishList, WhishListItem
from django.contrib import messages # type: ignore
from django.shortcuts import redirect # type: ignore
from Home.views import index, products_description

current_url = ''

# Création des informations du panier
def add_to_cart(request, slug):
    # current_url = request.resolver_match.view_name
    # current_url_match = request.resolver_match
    user = request.user  # On récupère les informations du client
    product = get_object_or_404(Product,
                                slug=slug)  # On récupère le slug du produit s'il existe sinon on lève une erreur
    cart, _ = Cart.objects.get_or_create(
        user=user)  # On récupère le panier de l'utilisateur s'il existe sinon on le crée
    order, created = Order.objects.get_or_create(user=user,
                                                 product=product)  # On récupère la commande de l'utilisateur s'il existe sinon on le crée

    # Si la commande n'existe pas, on la créée et on ajoute la commande sélectionnée
    if created:
        cart.orders.add(order)
        cart.save()
    # Si la commande n'existe pas, on la créée et on ajoute la commande sélectionnée

    # Si la commande existe déjà, on incrémente la quantité 
    else:
        order.quantity += 1
        order.save()
    # Si la commande existe déjà, on incrémente la quantité 

    return HttpResponseRedirect(reverse("products_description", kwargs={'slug': slug}))


def add_to_whishlist(request, slug):
    user = request.user # Récupère les informations de l'utilisateur
    product = get_object_or_404(Product, slug=slug)
    wishlist, _ = WishList.objects.get_or_create(user=user)
    whishList_item, created = WhishListItem.objects.get_or_create(user=user, product=product)
    

    wishlist.products.add(product)
    
    return HttpResponseRedirect(reverse("wishlist"))

# Gestion du panier
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'home/page/cart.html', context={"orders": cart.orders.all()})


def wishlist(request):
    wishlist_cart = get_object_or_404(WishList, user=request.user)
    return render(request, 'home/page/wishlist.html', context = {'products': wishlist_cart.products.all()})


def cart_delete(request):
    cart = request.user.cart
    if cart:
        cart.orders.all().delete()
        cart.delete()
        messages.success(request, "L'élément a été supprimé du panier.")
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
    return HttpResponseRedirect(reverse("products_description", kwargs={'slug': slug}))



def wishlist_article_delete(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    wishlist = get_object_or_404(WishList, user=user)
    
    wishlist.products.remove(product)
    
    messages.success(request, "L'article a été retiré de la liste d'envies.")
    return HttpResponseRedirect(reverse("wishlist"))