from django.db import models


# Create your models here.
class User(models.Model):
    u_id = models.IntegerField(unique=True)     # id是唯一的
    u_name = models.CharField(max_length=16)
    u_password = models.CharField(max_length=128)
    u_icon = models.ImageField(upload_to='icons')
