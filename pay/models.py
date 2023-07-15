from django.db import models
from django.contrib.auth.models import User
from settings.settings import AUTH_USER_MODEL
from store.models import Order, Product
from django.utils import timezone

# class Payment(models.Model):
#     user = models.ForeignKey(AUTH_USER_MODEL ,on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)

# class Payment(models.Model):
#     user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
#     articles = models.ForeignKey(Product, on_delete=models.CASCADE)
#     nom = models.CharField(max_length=50)
#     prenom = models.CharField(max_length=50)
#     telephone = models.CharField(max_length=20)
#     autre_telephone = models.CharField(max_length=20)
#     ville = models.CharField(max_length=50)
#     adresse = models.CharField(max_length=255, default='')
#     payment_method = models.CharField(max_length=50)
#     created_at = timezone.now()
    
#     def __str__(self):
#         return f"Commande #{self.id} - {self.user.username}"

