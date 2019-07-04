from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120) #max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "/products/{self.id}/"