from django import forms
from . models import *
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('profile_image',)

class AccountCreationForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())

