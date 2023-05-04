from django.shortcuts import get_object_or_404, render
from store.models import Product

# Create your views here.
def index(request):
    product = Product.objects.all()
    context = {'product' : product}
    return render(request, 'home/page/index.html', context)

def products_description(request, slug):
    product = Product.objects.get(slug=slug)
    product_details = Product.objects.all()
    context = {'product' : product, 'product_details' : product_details}
    return render(request, 'home/page/products_details.html', context)