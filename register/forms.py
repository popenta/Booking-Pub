from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from requests import request

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]


class EditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
    
    def clean_password(self):
        return self.clean_password


class PassChangeForm(PasswordChangeForm):

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
