from django.contrib.auth.models import User
from .models import HouseDetails
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
from django import forms

class userForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields: ['username', 'email', 'password']


class CityForm(forms.ModelForm):

    class Meta:
        model = HouseDetails
        fields = ("coordinates", "city_hall")
        widgets = {
            'coordinates': GooglePointFieldWidget,
            'city_hall': GoogleStaticOverlayMapWidget,
        }