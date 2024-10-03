from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Fruits(models.Model):
    fruit_name = models.CharField(max_length=255, blank=True)
    fruit_qty = models.IntegerField()
    fruit_created = models.DateTimeField(auto_now_add=True)
    fruit_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["id"]


