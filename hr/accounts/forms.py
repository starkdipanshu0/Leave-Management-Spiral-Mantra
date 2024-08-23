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
            'class': 'mt-1 block w-full px-3 py-2 text-sm text-gray-900 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600 dark:focus:ring-blue-500',  # Custom class for styling
            'placeholder': 'Enter your username'
        })
	)
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 text-sm text-gray-900 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600 dark:focus:ring-blue-500',  # Custom class for styling
            'placeholder': 'Enter your password'
        })
	)


