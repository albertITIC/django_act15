from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.get_all_products, name='list_products'),  # Obtener todos los productos
    path('products/create/', views.create_product, name='create_product'),  # Crear un producto
    path('products/<int:pk>/', views.get_product_by_id, name='get_product'),  # Obtener un producto
    path('products/<int:pk>/update/', views.update_product, name='update_product'),  # Actualizar producto
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),  # Eliminar producto
]
