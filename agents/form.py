from django import forms
from .models import UserMessage

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=40)
    email = forms.EmailField()
    phone = forms.CharField(max_length=40)
    message = forms.Textarea()
    email_user = forms.EmailField()

    class Meta:
        model = UserMessage
        fields = ('name', 'email', 'phone', 'message', 'email_user')
