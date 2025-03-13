from django.urls import path
from .views import *


urlpatterns = [
    path('', course_list, name="courses"),
    path('add_course', course_form, name="add_course"),
    path('update_course/<int:course_id>/', course_update, name='course_update'),
    path('course_delete/<int:course_id>/', course_delete, name='course_delete')
    
]
