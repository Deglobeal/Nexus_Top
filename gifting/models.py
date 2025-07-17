from django.db import models
from django.conf import settings

# Create your models here.
class Gifting (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gift_type = models.CharField(max_length=15, choices = [('airtime', 'Airtime'), ('data', 'Data'), ('gift_card', 'Gift Card')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    recipient = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    network = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)                                                      