from django.urls import path
from .views import *

urlpatterns = [
    path('', trainee_list, name="trainee"),
    path('add_trainee', trainee_form, name="add_trainee")
]
