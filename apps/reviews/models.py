from tkinter import CASCADE
from django.db import models
from apps.products.models import Product

# Create your models here.
class Review(models.Model):
    author = models.CharField(max_length=256)
    review = models.TextField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)