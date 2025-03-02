from django.urls import path
from . import views

urlpatterns = [
    path('order_history/', views.order_history, name='order_history'),  # Historial de órdenes
    path('unfinished_carts/', views.unfinished_carts, name='unfinished_carts'),  # Carritos no finalizados
]