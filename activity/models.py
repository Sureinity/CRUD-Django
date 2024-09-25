from django.db import models

# Create your models here.
class Fruits(models.Model):
    fruit_name = models.CharField(max_length=255, blank=True)
    fruit_qty = models.IntegerField(default=0, blank=True)
    fruit_created = models.DateField(auto_now=True)
    fruit_updated = models.DateField(auto_now=True)
