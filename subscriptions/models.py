from django.db import models

# Create your models here.
class Subscriptionplan(models.Model):
    user = models.CharField(max_length=100)
    plan_name = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=50, choices=[('daily', 'Daily'), ('monthly', 'Monthly'), ('yearly', 'Yearly')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)   
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('expired', 'Expired')], default='active')
    