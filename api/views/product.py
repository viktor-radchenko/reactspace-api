from django.views.decorators.cache import cache_page
from platformdirs import api
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Product
from api.serializers import ProductSerializer


@cache_page(60)
@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist as e:
        return Response({'detail': str(e)})
