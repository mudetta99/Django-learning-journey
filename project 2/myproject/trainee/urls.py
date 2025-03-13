from django.urls import path
from .views import *

urlpatterns = [
    path('', trainee_list, name="trainee"),
    path('add_trainee', trainee_form, name="add_trainee"),
    path('update_trainee/<int:trainee_id>/', trainee_update, name='update_trainee'),
    path('delete_trainee/<int:trainee_id>/', trainee_delete, name='delete_trainee')
]


