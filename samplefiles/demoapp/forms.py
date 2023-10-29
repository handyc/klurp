from django import forms


class SimpleForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')
    witness = forms.CharField(max_length=100)
    common = forms.BooleanField(required=False)
    common2 = forms.BooleanField(required=False)
    common3 = forms.BooleanField(required=False)
