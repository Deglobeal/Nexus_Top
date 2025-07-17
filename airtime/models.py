from django.db import models

# Create your models here.
class Airtime(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    network = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='pending')