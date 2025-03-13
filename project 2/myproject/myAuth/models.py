from django.db import models

# Create your models here.

class MyAuth(models.Model):
    username = models.CharField(max_length=20, null=False)
    email = models.EmailField(unique=True,  null=False)
    password = models.CharField(max_length=50, null=False)

