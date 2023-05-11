from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name
