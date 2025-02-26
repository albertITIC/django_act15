from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Crear un router para generar automáticamente las rutas de la API
router = DefaultRouter()
router.register(r'products', ProductViewSet)  # Registrar el ViewSet con la URL 'products'

urlpatterns = [
    path('api/', include(router.urls)),  # Incluir todas las rutas generadas por el router
]
