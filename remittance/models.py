from django.db import models

# Create your models here.

class Remittance(models.Model):
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)  # e.g., "USD", "EUR"
    remittance_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')  # e.g., "pending", "completed", "failed"
    transaction_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    