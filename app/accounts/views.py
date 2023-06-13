from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomProfileChangeForm, CustomUserCreationForm


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "account/signup.html"
    success_message = "The account was registered successfully."


class ProfileUpdateView(UpdateView):
    form_class = CustomProfileChangeForm
    success_url = reverse_lazy("home")
    template_name = "account/profile_edit.html"

    def get_object(self, queryset=None):
        return self.request.user
