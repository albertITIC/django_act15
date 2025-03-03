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
    """ Procesar el pago de una orden con autenticación """
    
    # Verificar si el usuario está autenticado
    if not request.user or not request.user.is_authenticated:
        return JsonResponse({"error": "Debes iniciar sesión para realizar un pago"}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = PaymentSerializer(data=request.data)

    if serializer.is_valid():
        order_id = request.data.get("order")
        try:
            # Asegurarse de que la orden corresponde al usuario autenticado
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Orden no encontrada o no pertenece al usuario"}, status=status.HTTP_404_NOT_FOUND)

        # Guardar pago con estado 'approved'
        payment = serializer.save(status="approved")

        # Actualizar estado de la orden
        order.status = "paid"
        order.save()

        return JsonResponse({"message": "Pago exitoso", "payment_id": payment.id}, status=status.HTTP_201_CREATED)
    
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)