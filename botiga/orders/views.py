from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Order
from cart.models import Cart
# Create your views here.

@api_view(['GET'])
def order_history(request):
    """
    Mostrar el historial de órdenes del usuario autenticado.
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

    # Obtener todas las órdenes del usuario autenticado
    orders = Order.objects.filter(user=request.user)

    # Serializar las órdenes
    order_list = []
    for order in orders:
        order_data = {
            "order_id": order.id,
            "total_price": str(order.total_price),
            "status": order.status,
            "created_at": order.created_at,
        }
        order_list.append(order_data)

    return JsonResponse({"orders": order_list}, status=status.HTTP_200_OK)

@api_view(['GET'])
def unfinished_carts(request):
    """
    Mostrar los carritos no finalizados (aquellos cuyo estado no es 'purchased' o 'finalizado').
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

    # Obtener todos los carritos no finalizados
    unfinished_carts = Cart.objects.filter(status__in=['active', 'pending'])

    # Serializar los carritos
    cart_list = []
    for cart in unfinished_carts:
        cart_data = {
            "cart_id": cart.id,
            "status": cart.status,
            "created_at": cart.created_at,
        }
        cart_list.append(cart_data)

    return JsonResponse({"unfinished_carts": cart_list}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_unfinished_cart(request, pk):
    """
    Eliminar un carrito no finalizado (con estado 'active' o 'pending').
    """
    try:
        cart = Cart.objects.get(id=pk)
    except Cart.DoesNotExist:
        return JsonResponse({"error": "Carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # Verificar si el carrito está en un estado que puede ser eliminado
    if cart.status not in ['active', 'pending']:
        return JsonResponse({"error": "El carrito no puede ser eliminado porque ya está finalizado"}, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar el carrito
    cart.delete()

    return JsonResponse({"message": "Carrito eliminado con éxito"}, status=status.HTTP_204_NO_CONTENT)