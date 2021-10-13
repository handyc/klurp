from django import forms
from django.forms import ModelForm

from .models import Dictionary
from .models import DictionaryEntry

class SimpleForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')
    witness = forms.CharField(max_length=100)
    common = forms.BooleanField(required=False)
    common2 = forms.BooleanField(required=False)
    common3 = forms.BooleanField(required=False)

