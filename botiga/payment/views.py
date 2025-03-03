from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from orders.models import Order
# Create your views here.
@api_view(['POST'])
def process_payment(request):
    """ Procesar el pago de una orden """
    serializer = PaymentSerializer(data=request.data)

    if serializer.is_valid():
        order_id = request.data.get("order")
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Orden no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        # Guardar pago con estado approved
        payment = serializer.save(status="approved")

        # Actualizar estado de la orden
        order.status = "paid"
        order.save()

        return JsonResponse({"message": "Pago exitoso", "payment_id": payment.id}, status=status.HTTP_201_CREATED)
    
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)