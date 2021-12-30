from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password = forms.CharField (widget=forms.PasswordInput())
    class Meta :
        model = CustomUser
        fields = ('firstname', 'lastname', 'email', 'username', 'password')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
