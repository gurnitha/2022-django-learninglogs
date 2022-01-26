# learning_logs/forms.py

# Django modules
from django import forms

# Locals
from .models import Topic

# Create your form here.

# Form: TopicForm
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}