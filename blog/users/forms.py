from django import forms 
from django.contrib.auth import models 
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class User(forms.Form):
    username = forms.CharField(max_length=150 )
    password = forms.CharField(max_length=120 , widget = forms.PasswordInput() )

class SignUp(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150) 
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(max_length = 150, widget = forms.PasswordInput())
    confirm_password = forms.CharField(max_length=150, widget=forms.PasswordInput())

    def clean_username(self):
        if UserModel.objects.filter(username = self.cleaned_data['username']).exists():
            raise forms.ValidationError('Username already exists')
        return self.cleaned_data['username']
    
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords don\'t match')
        return self.cleaned_data 