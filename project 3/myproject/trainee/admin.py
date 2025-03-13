from django.contrib import admin

# Register your models here.

from .models import *

class CourseTrainee(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'age')
    search_fields = ('email', 'joined_date')
    list_filter = ('age', 'joined_date', 'activate')


admin.site.register(Trainee, CourseTrainee)









    # list_display = ('name', 'duration', 'level') 
    # search_fields = ('name', 'level') 
    # list_filter = ('level',)  
