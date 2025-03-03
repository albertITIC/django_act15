from rest_framework import serializers
from .models import Order, OrderItem
from cart.serializers import CartSerializer
from catalog.serializers import ProductSerializer  

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer() 

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)  
    cart = CartSerializer() 

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'created_at', 'items', 'cart']