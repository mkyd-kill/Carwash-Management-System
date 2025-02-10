from django import forms
from .models import SiteAdmin, Services, Staff

class AdminForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    hashed_password = forms.CharField(max_length=100)