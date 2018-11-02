from rest_framework import serializers

from .models import Product, Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name', 'birthday']


class ProductSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(read_only=True)
    date_updated = serializers.DateField(read_only=True)
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    description = serializers.CharField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'seller', 'date_added', 'date_updated']
