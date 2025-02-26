from django.db import models

# Create your models here.
from ..orders.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvc = models.CharField(max_length=3)
    status = models.CharField(max_length=50)