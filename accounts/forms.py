from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import keyid
from django.core import validators


class UserForm(UserCreationForm):

    def clean_email(self):
        email=self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already registered')


    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class keyForm(forms.ModelForm):

    class Meta:
        model = keyid
        exclude=('keys','user')
