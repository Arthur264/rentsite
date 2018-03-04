from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SingUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
