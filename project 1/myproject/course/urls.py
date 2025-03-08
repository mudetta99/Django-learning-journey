from django.urls import path
from .views import *


urlpatterns = [
    path('', course_list, name="courses"),
    path('add_course', course_form, name="add_course"),
    
]


