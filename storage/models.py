from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
