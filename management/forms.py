from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SiteAdmin, Services, Staff
    
class AdminCreationForm(UserCreationForm):
    class Meta:
        model = SiteAdmin
        fields = ['username', 'password1', 'password2']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            "name", "national_id", "email", "gender", "role", "department", "contact", "commission", "salary", "status"
        ]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = [
            "name", "cost", "discount", "status", "availability"
        ]