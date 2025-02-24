from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)                       # Nombre del producto
    description = models.TextField(blank=True)                    # Descripción opcional
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio
    stock = models.IntegerField()                                 # Cantidad en stock
    category = models.CharField(max_length=100)                   # Categoría del producto
    image = models.CharField(max_length=255, blank=True)          # URL de la imagen (opcional)

# def __str__(self):
#     return self.name