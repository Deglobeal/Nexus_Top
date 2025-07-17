from django.db import models

# Create your models here.
class DataBundle(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    data_plan = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
