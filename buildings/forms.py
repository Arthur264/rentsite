from django.contrib.auth.models import User
from .models import HouseDetails, House
from mapwidgets.widgets import GooglePointFieldWidget
from django import forms


class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CityAdminForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ("title")
        widgets = {
            'title': GooglePointFieldWidget,
            # 'city_hall': GooglePointFieldWidget,
        }