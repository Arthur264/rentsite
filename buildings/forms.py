from django.contrib.auth.models import User
from .models import HouseDetails, House, HouseLocation
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
from django import forms


class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CityForm(forms.ModelForm):
    class Meta:
        model = HouseLocation
        fields = ("location",)
        widgets = {
            'location': GooglePointFieldWidget
        }