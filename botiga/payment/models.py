from django.db import models
from django.core.exceptions import ValidationError
import datetime
# Create your models here.
from orders.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvc = models.CharField(max_length=3)
    status = models.CharField(max_length=50)

    def clean(self):
        """ Validaciones personalizadas """
        # Validar número de tarjeta (debe ser numérico y de 16 dígitos)
        if not self.card_number.isdigit() or len(self.card_number) != 16:
            raise ValidationError("El número de tarjeta debe tener 16 dígitos numéricos.")

        # Validar CVC (debe ser numérico y de 3 dígitos)
        if not self.cvc.isdigit() or len(self.cvc) != 3:
            raise ValidationError("El CVC debe tener 3 dígitos numéricos.")

        # Validar fecha de expiración (no puede estar en el pasado)
        if self.expiration_date < datetime.date.today():
            raise ValidationError("La tarjeta ha expirado.")

    def save(self, *args, **kwargs):
        """ Ejecutar validaciones antes de guardar """
        self.clean()
        super().save(*args, **kwargs)