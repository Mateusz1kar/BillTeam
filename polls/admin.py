from django.contrib import admin
from .models import  Project ,Person2, Notification
# Register your models here.

admin.site.register(Person2)

admin.site.register(Project)
admin.site.register(Notification)