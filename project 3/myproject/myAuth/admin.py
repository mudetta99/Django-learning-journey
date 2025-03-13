from django.contrib import admin
from .models import MyAuth

# Register your models here.

class MyAuthAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(MyAuth, MyAuthAdmin)