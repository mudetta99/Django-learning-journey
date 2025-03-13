from django.db import models

# Create your models here.


class Course(models.Model):

    level_choices = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ]


    name = models.CharField(max_length=100, unique=True, null=False)
    duration = models.CharField(max_length=50, null=False)
    level = models.CharField(max_length=50, choices=level_choices)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    activate = models.BooleanField(default=True)

