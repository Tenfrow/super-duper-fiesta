from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return '{} (seller: {})'.format(self.name, self.seller)
