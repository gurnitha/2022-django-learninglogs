# users/url.py

"""Defines URL patterns for users."""

# Django modules
from django.urls import path, include

# Locals
from . import views

app_name = 'users'
urlpatterns = [
	# Include default auth urls.
	path('', include('django.contrib.auth.urls')),
]