from django import forms
from django.contrib.auth.models import User
from .models import *


class userloginform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }