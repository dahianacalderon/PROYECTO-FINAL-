from dataclasses import fields
from django import forms
from django.core import validators

# Import users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# forms users
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']