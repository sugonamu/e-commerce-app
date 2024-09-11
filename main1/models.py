from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # New field for image

    def __str__(self):
        return self.name
