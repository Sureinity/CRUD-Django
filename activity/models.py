from django.db import models

# Create your models here.
class User(models.Model):
    ADMIN = 1
    USER = 2
    VIEWER = 3

    CHOICES = (
        (ADMIN, "admin"),
        (USER, "user"),
        (VIEWER, "viewer")
    )

    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=128)
    role = models.IntegerField(choices=CHOICES, default=USER)
    

class Fruits(models.Model):
    fruit_name = models.CharField(max_length=255, blank=True)
    fruit_qty = models.IntegerField()
    fruit_created = models.DateTimeField(auto_now_add=True)
    fruit_updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ["id"]


