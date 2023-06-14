from django import forms
from django.contrib.auth import get_user_model

from .models import Comment, Task

User = get_user_model()


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


class TaskCompletionForm(forms.Form):
    completed = forms.BooleanField(widget=forms.HiddenInput())


class TaskPendingUsersForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["pending_users"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["pending_users"].queryset = User.objects.exclude(
                pk=user.pk
            )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "text",
        ]
