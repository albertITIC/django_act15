from django.urls import path
from . import views

urlpatterns = [
    path('order_history/', views.order_history, name='order_history'),  # Historial de órdenes
    path('unfinished_carts/', views.unfinished_carts, name='unfinished_carts'),  # Carritos no finalizados
    path('delete_unfinished_cart/<int:pk>/', views.delete_unfinished_cart, name='delete_unfinished_cart'),  # Eliminar carrito no finalizado
]