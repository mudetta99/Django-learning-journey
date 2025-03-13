from django.db import models
from course.models import Course
# Create your models here.

class Trainee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    age = models.PositiveIntegerField()
    joined_date = models.DateField()
    activate = models.BooleanField(default=True)




