# learning_logs/admin.py

# Django modules
from django.contrib import admin

# Locals
from .models import Topic  

# Register your models here.


admin.site.register(Topic)