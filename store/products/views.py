from rest_framework import generics

from products.models import Product
from products.serializers import (ProductDetailsSerializer,
                                  ProductListSerializer)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
