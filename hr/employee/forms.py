from django import forms
from employee.models import Role,Department,CustomUser
from django.contrib.auth.models import User


# EMPLOYEE
class EmployeeCreateForm(forms.ModelForm):
	employeeid = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'please enter 5 characters without RGL or slashes eg. A0025'}))
	image = forms.ImageField(widget=forms.FileInput(attrs={'onchange':'previewImage(this);'}))
	class Meta:
		model = CustomUser
		exclude = ['is_blocked','is_deleted','created','updated']
		widgets = {
				'bio':forms.Textarea(attrs={'cols':5,'rows':5})
		}

