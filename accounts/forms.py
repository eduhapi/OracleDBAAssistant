from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'pno', 'email']

class CustomAuthenticationForm(AuthenticationForm):
    pno = forms.CharField(max_length=20, label='Personal Number')
