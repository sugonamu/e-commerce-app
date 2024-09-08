from django.db import models
from django.utils import timezone

class Product(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.nama
