from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import keyid

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class keyForm(forms.ModelForm):

    class Meta:
        model = keyid
        exclude=('keys','user')
