from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    is_active = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_active']
        extra_kwargs = {'is_active': {'value': False}}
