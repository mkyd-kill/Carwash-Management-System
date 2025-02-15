from django import forms
from .models import SiteAdmin, Services, Staff
from django.contrib.auth.hashers import make_password

class AdminForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = SiteAdmin
        fields = ['username', 'email', 'passsword']

    def clean_username(self):
        username = self.cleaned_data["username"]
        if SiteAdmin.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken. Try another one.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if SiteAdmin.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already taken. Try another one.")
        return email
    
    def save(self, commit=True):
        user = SiteAdmin()
        user.password = make_password(self.cleaned_data["password"])
        user.is_active = False
        if commit:
            user.save()
        return user
    

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