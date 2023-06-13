from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
            "telegram",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
            "telegram",
        )


class CustomProfileChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "telegram",
        )
