from django.contrib import admin

# Register your models here.

from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'level') 
    search_fields = ('name', 'level') 
    list_filter = ('level',)  

admin.site.register(Course, CourseAdmin)



