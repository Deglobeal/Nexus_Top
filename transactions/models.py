from django.db import models
from django.conf import settings

# Create your models here.
class Trsnsaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=[('credit', 'Credit'), ('debit', 'Debit')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
    reference_id = models.CharField(max_length=100, unique=True)
    transaction_date = models.DateTimeField(auto_now_add=True)

