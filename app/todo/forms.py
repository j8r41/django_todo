from django import forms
from multiupload.fields import MultiFileField
from .models import Task


class TaskForm(forms.ModelForm):
    files = MultiFileField(min_num=1, max_num=10)

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["files"].widget.attrs["multiple"] = True
