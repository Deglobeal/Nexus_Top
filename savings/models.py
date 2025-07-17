from django.db import models

# Create your models here.
class SavingsCircle(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    account_type = models.CharField(max_length=50)  # e.g., "savings", "fixed deposit"
    target_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
