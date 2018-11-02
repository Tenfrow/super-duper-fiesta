from rest_framework import generics

from storage.models import Seller
from storage.serializers import SellerSerializer


class SellerList(generics.ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
