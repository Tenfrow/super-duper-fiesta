from rest_framework import serializers

from .models import Product, Seller


class ProductSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(read_only=True)
    date_updated = serializers.DateField(read_only=True)
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    description = serializers.CharField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'seller', 'date_added', 'date_updated']


class ProductSimpleSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'date_added', 'date_updated']


class SellerSerializer(serializers.ModelSerializer):
    products = ProductSimpleSerializer(many=True)

    class Meta:
        model = Seller
        fields = ['id', 'name', 'birthday', 'products']
        depth = 1
