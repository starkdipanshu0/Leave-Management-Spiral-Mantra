from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.conf import settings
from django.db.models import Q
import datetime
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse
from employee.forms import EmployeeCreateForm
from leave.models import Leave
from employee.models import *
from leave.forms import LeaveCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def dashboard(request):
    emp_count = Employee.objects.all().count()
    leave_count = Leave.objects.all().count()
    context ={
        'emp_count':emp_count,
        'leave_count':leave_count
    }
    return render(request,'Admin/dashboard.html',context)

def leave_application(request):
    leaves_list = Leave.objects.all()
    return render(request,'Admin/leave_application.html', {'leaves_list': leaves_list})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'Admin/employee_list.html', {'employees': employees})
