from django.db import models
from django.contrib.auth.models import User
from settings.settings import AUTH_USER_MODEL
from store.models import Order

# class Payment(models.Model):
#     user = models.ForeignKey(AUTH_USER_MODEL ,on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # Autres champs liés au paiement
