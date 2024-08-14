from django import forms
from .models import Leave
import datetime
class LeaveCreationForm(forms.ModelForm):
    reason = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'mt-1 block w-full px-3 py-2 text-sm text-gray-900 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600 dark:focus:ring-blue-500',  # Custom class for styling
            'rows': 4,
            'cols': 40,
            'placeholder': 'Enter the reason for leave'
        })
    )
    startdate = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 text-sm text-gray-900 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600 dark:focus:ring-blue-500',  # Custom class for styling
            'type': 'date',
            'placeholder': 'Start Date'
        })
    )
    enddate = forms.DateField(
    widget=forms.DateInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 text-sm text-gray-900 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600 dark:focus:ring-blue-500',
        'type': 'date',
        'placeholder': 'End Date'
    })
    )

    leavetype = forms.ChoiceField(

        choices=Leave.LEAVE_TYPE,  # Replace with your actual choices
        widget=forms.Select(attrs={
            'class': 'mt-1 block w-full px-3 py-2 text-sm text-gray-900 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600 dark:focus:ring-blue-500',  # Custom class for styling
        })
    )

    class Meta:
        model = Leave
        exclude = ['user', 'defaultdays', 'hrcomments', 'status', 'is_approved', 'updated', 'created']

    def clean_enddate(self):
        enddate = self.cleaned_data.get('enddate')
        startdate = self.cleaned_data.get('startdate')
        today_date = datetime.date.today()

        if (startdate or enddate) < today_date:
            raise forms.ValidationError("Selected dates are incorrect, please select again")

        elif startdate >= enddate:
            raise forms.ValidationError("End date must be after the start date")

        return enddate



