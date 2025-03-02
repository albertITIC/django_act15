from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# CREAR UN PRODUCTE (POST)
@api_view(['POST'])
def create_product(request):
    # Endpoint per afegir un nou producte a la base de dades.
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# OBTENIR TOTS ELS PRODUCTES (GET)
@api_view(['GET'])
def get_all_products(request):
    # Endpoint per obtenir tots els productes de la base de dades.
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# OBTENIR UN PRODUCTE PER ID (GET)
@api_view(['GET'])
def get_product_by_id(request, product_id):
    # Endpoint per obtenir un producte concret a partir del seu ID. Si no troba l'error envia un error 404
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "Producte no trobat"}, status=status.HTTP_404_NOT_FOUND)

# ACTUALITZAR UN PRODUCTE (PUT, PATCH)
@api_view(['PUT', 'PATCH'])
def update_product(request, product_id):
    # Endpoint per actualitzar un producte existent.
    # PUT -> Actualitza TOT el producte. PATCH -> Només modifica els camps indicats.
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Producte no trobat"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data, partial=(request.method == 'PATCH'))

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ELIMINAR UN PRODUCTE (DELETE)
@api_view(['DELETE'])
def delete_product(request, product_id):
    # Endpoint per eliminar un producte de la base de dades.
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response({"message": "Producte eliminat correctament"}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({"error": "Producte no trobat"}, status=status.HTTP_404_NOT_FOUND)