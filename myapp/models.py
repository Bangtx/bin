from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=30)
    passw = models.CharField(max_length=10)