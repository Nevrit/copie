from django.db import models
from django_extensions.db.fields import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from settings.settings import AUTH_USER_MODEL
from django.utils import timezone

# Création des catégories d'articles qui seront reliées aux produits
class Category(MPTTModel):
    name = models.CharField(max_length=228, unique=False)
    mark = models.CharField(max_length=50, default='', blank=True, verbose_name='Marque')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name', 'mark']
    
    def __str__(self):
        return self.name
# Création des catégories d'articles qui seront reliées aux produits


# Création des produits. Un produit sera lié à une catégorie d'article
class Product(models.Model):
    name = models.CharField(max_length=50)
    title = models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(default=0.0)
    old_price = models.FloatField(default=0.0)
    stock_quantity = models.IntegerField(default=0)
    description = RichTextField(blank=True)
    technical_information = RichTextField(blank=True, default='', verbose_name="Fiche technique")
    image = models.ImageField(upload_to='products', blank=True, null=True)
    slug = AutoSlugField(populate_from=['name'])
    
    def __str__(self):
        return self.name
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
# Création des produits. Un produit sera lié à une catégorie d'article

# Création de la galerie pour les images
class Galery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    title = models.CharField(max_length=80, blank=True)
    
    def __str__(self):
        return self.title
# Création de la galerie pour les images
    

# Création des commandes des utilisateurs  
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL ,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.product.name} ({self.quantity})' 
# Création des commandes des utilisateurs  

# Création du panier de l'utilisateur, un utilisateur aura un panier  
class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    
    def __str__(self):
        return self.user.email 
    
    # def delete(self, *args, **kwargs):
    #     for order in self.orders.all():
    #         order.ordered = True
    #         order.ordered_date = timezone.now()
    #         order.save()
        
    #     self.orders.clear()
    #     super().delete(*args, **kwargs)
# Création du panier de l'utilisateur, un utilisateur aura un panier 