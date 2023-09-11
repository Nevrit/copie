from django.shortcuts import get_object_or_404, render
from store.models import Cart, Order, Product

# Create your views here.
def index(request):
    product = Product.objects.all()
    context = {'product' : product}
    return render(request, 'home/page/index.html', context)

def products_description(request, slug):
    product = Product.objects.get(slug=slug)
    product_details = Product.objects.all()
    cart = Cart.objects.all()
    total_price = ''
    
    # Afficher la commande du client connecté
    if request.user.is_authenticated:
        commande = Order.objects.filter(user=request.user, ordered=False)
        total_price = 0
        for order in commande:
            total_price += order.product.price * order.quantity
    else:
        commande = []
    # Afficher la commande du client connecté
        
    context = {'product' : product, 'product_details' : product_details, 'commande' : commande, 'cart' : cart, 'total_price' : total_price}
    return render(request, 'home/page/products_details.html', context)
