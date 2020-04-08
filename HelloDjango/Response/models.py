from django.db import models


# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=128)
    u_token = models.CharField(max_length=256)
