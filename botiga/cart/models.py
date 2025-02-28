from django.db import models
from catalog.models import Product

class Cart(models.Model):
    user = models.ForeignKey("orders.CustomUser", on_delete=models.CASCADE)  # Referencia en cadena
    created_at = models.DateTimeField(auto_now_add=True) 

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()