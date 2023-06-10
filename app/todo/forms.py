from django import forms
from django.contrib.auth.models import User

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


class TaskAssignedUsersForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["assigned_users"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["assigned_users"].queryset = User.objects.exclude(
                pk=user.pk
            )
