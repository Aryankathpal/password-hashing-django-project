from django import forms
from .models import encoded

class encodeForm(forms.ModelForm):

    class Meta:
        model = encoded
        fields = ('name','password')
