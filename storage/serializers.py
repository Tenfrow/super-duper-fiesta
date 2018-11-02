from rest_framework import serializers

from .models import Product, Seller


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
