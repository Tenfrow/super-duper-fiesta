from rest_framework import generics

from storage.models import Seller, Product
from storage.serializers import SellerSerializer, ProductSerializer


class SellerList(generics.ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
