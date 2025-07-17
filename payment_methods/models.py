from django.db import models

# Create your models here.
class Payment_Method(models.Model):
    user = models.CharField(max_length=100, blank=True, null=True)
    payment_type = models.CharField(max_length=50) # still need to be defined 
    name = models.CharField(max_length=100)
    details = models.JSONField(blank=True, null=True)  # Store payment details as JSON
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
