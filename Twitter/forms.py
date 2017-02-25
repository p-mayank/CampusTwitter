from django import forms
from django.contrib.auth.models import User
from .models import useradd, tweet, comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    profile_picture = forms.FileField(required=False)

    class Meta:
        model = useradd
        fields = ['username', 'email', 'password', 'country', 'profile_picture']
        help_texts = None

class TweetForm(forms.ModelForm):

    class Meta:
        model = tweet
        fields = ['text', 'tweetto']

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['ctext']
