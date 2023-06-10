from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "end_date",
            "status",
            "files",
        ]
        widgets = {
            "end_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
