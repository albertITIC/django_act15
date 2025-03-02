from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from catalog.models import Product
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
# Create your views here.

@api_view(['GET'])
def get_cart(request, pk):
    """
    Obtener el carrito de compras por id.
    """
    try:
        cart = Cart.objects.get(id=pk)
    except Cart.DoesNotExist:
        return JsonResponse({"error": "Carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CartSerializer(cart)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def add_item(request, pk):
    """
    Añadir un producto al carrito.
    """
    try:
        cart = Cart.objects.get(id=pk)
    except Cart.DoesNotExist:
        return JsonResponse({"error": "Carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    product_id = request.data.get('product')
    quantity = int(request.data.get('quantity', 1))

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    item.quantity += quantity
    item.save()

    return JsonResponse(CartItemSerializer(item).data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def remove_item(request, pk):
    """
    Eliminar un producto del carrito.
    """
    try:
        cart = Cart.objects.get(id=pk)
    except Cart.DoesNotExist:
        return JsonResponse({"error": "Carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    product_id = request.data.get('product')

    try:
        item = CartItem.objects.get(cart=cart, product_id=product_id)
        item.delete()
        return JsonResponse({"message": "Producto eliminado del carrito"}, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return JsonResponse({"error": "El producto no está en el carrito"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_quantity(request, pk):
    """
    Modificar la cantidad de un producto en el carrito.
    """
    try:
        cart = Cart.objects.get(id=pk)
    except Cart.DoesNotExist:
        return JsonResponse({"error": "Carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    product_id = request.data.get('product')
    quantity = int(request.data.get('quantity', 1))

    try:
        item = CartItem.objects.get(cart=cart, product_id=product_id)
        if quantity > 0:
            item.quantity = quantity
            item.save()
            return JsonResponse(CartItemSerializer(item).data, status=status.HTTP_200_OK)
        else:
            item.delete()
            return JsonResponse({"message": "Producto eliminado del carrito"}, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return JsonResponse({"error": "El producto no está en el carrito"}, status=status.HTTP_404_NOT_FOUND)