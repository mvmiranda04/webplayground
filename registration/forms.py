from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 caracteres como máximo y debe ser un email "
                                                      "válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")