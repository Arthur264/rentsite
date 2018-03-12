from django import forms
from models import Comments


class CommentForm(forms.ModelForm):
    comment = forms.Textarea()
    author = forms.CharField(max_length=40)
    email = forms.EmailField()
    news = forms.CharField()
    website = forms.CharField(max_length=100)

    class Meta:
        fields = ('comment', 'author', 'email', 'website', 'news')
        model = Comments
