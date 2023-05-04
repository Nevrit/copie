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
    order = Order.objects.all()
    context = {'product' : product, 'product_details' : product_details, 'cart' : cart, 'order' : order}
    return render(request, 'home/page/products_details.html', context)