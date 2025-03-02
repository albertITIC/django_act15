from django.urls import path
from . import views

urlpatterns = [
    path('cart/<int:pk>/', views.get_cart, name='get_cart'),  # Obtener carrito
    path('cart/<int:pk>/add_item/', views.add_item, name='add_item'),  # Añadir producto al carrito
    path('cart/<int:pk>/remove_item/', views.remove_item, name='remove_item'),  # Eliminar producto del carrito
    path('cart/<int:pk>/update_quantity/', views.update_quantity, name='update_quantity'),  # Modificar cantidad en el carrito
    path('cart/<int:pk>/checkout/', views.checkout, name='checkout'), # Gestionar comprar carrito
]