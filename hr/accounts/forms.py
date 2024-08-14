from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit




class UserRegistrationForm(UserCreationForm):
	'''
	Extending UserCreationForm - with email

	'''

	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'eg.rajparmar@.com'}))

	class Meta:
		model = User
		fields = ['username','email','password1','password2']





class UserLogin(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(attrs={
            'class': 'form-input',  # Custom class for styling
            'placeholder': 'Enter your username'
        })
	)
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={
            'class': 'form-input',  # Custom class for styling
            'placeholder': 'Enter your password'
        })
	)


