from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic


from .forms import CustomUserCreationForm


class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "The account was registered successfully."
