from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomProfileChangeForm(forms.ModelForm):
    telegram_key = forms.CharField(
        widget=forms.TextInput(attrs={"readonly": True}),
        help_text="This field is auto-generated and cannot be edited.",
    )

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "telegram_key",
        )
