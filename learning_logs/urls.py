# learning_logs/url.py

"""Defines URL patterns for learning_logs."""

# Django modules
from django.urls import path

# Locals
from . import views

app_name = 'learning_logs'
urlpatterns = [
	# Home page
    path('', views.index, name='index'),
]
