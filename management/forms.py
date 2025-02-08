from django import forms

class DataForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.PasswordInput()