from rest_framework import serializers
from .models import Payment
import datetime

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def validate_card_number(self, value):
        """ Validar que el número de tarjeta tenga 16 dígitos numéricos """
        if not value.isdigit() or len(value) != 16:
            raise serializers.ValidationError("El número de tarjeta debe tener 16 dígitos numéricos.")
        return value

    def validate_cvc(self, value):
        """ Validar que el CVC tenga 3 dígitos numéricos """
        if not value.isdigit() or len(value) != 3:
            raise serializers.ValidationError("El CVC debe tener 3 dígitos numéricos.")
        return value

    def validate_expiration_date(self, value):
        """ Validar que la tarjeta no esté expirada """
        if value < datetime.date.today():
            raise serializers.ValidationError("La tarjeta ha expirado.")
        return value
