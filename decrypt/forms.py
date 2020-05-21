from django import forms
from django.contrib.auth.models import User
from .models import decode

class decrypt(forms.ModelForm):
    class Meta:
        model = decode
        fields = ('encrypted_password',)
