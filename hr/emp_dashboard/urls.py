from django.urls import path
from . import views

app_name = 'emp_dashboard'

urlpatterns = [
    path('dashboard/',views.employee_dashboard,name='dashboard'),
    path('apply_for_leave/',views.apply_for_leave,name='apply_for_leave'),
]

