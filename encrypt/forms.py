from django import forms
from .models import encoded

class encodeForm(forms.ModelForm):

    class Meta:
        model = encoded
        fields = ('name','password')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].label = 'Password Name'
