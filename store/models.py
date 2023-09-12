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


# Création des éléments du panier utilisateur CART_ITEM
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'
# Création des éléments du panier utilisateur CART_ITEM


# Création du panier de l'utilisateur, un utilisateur aura un panier
class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.email
# Création du panier de l'utilisateur, un utilisateur aura un panier


# Les commandes de l'utilisateur
class OrderOrder(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=255, verbose_name="Nom de famille")
    firstname = models.CharField(max_length=255, verbose_name="Prénom")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    another_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Autre téléphone")
    city = models.CharField(max_length=255, verbose_name="Ville")
    delivery_address = models.CharField(max_length=512, verbose_name="Adresse de livraison")
    payment_method = models.CharField(max_length=100, verbose_name="Methode de paiement")
    ordered_date = models.DateTimeField(blank=True, null=True)

    # Optionnel je peux afficher le montant total de la commande

    def __str__(self):
        return f"Commande de {self.firstname} {self.lastname}"

    class Meta:
        verbose_name = "Commande d'utilisateur"
        verbose_name_plural = "Commandes d'utilisateurs"


# Les commandes de l'utilisateur


# Récupération des articles contenues dans le panier Ordered_Item
class OrderedItem(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey(OrderOrder, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0.0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'
# Récupération des articles contenues dans le panier Ordered_Item