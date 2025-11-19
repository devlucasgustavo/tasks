from django import forms
from . import models


class TaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = ['title', 'description', 'category', 'priority', 'is_completed']


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = ['name', 'description']
