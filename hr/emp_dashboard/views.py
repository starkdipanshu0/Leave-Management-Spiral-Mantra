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

@login_required
def employee_dashboard(request):
    user = request.user
    employee = get_object_or_404(Employee, user=user)
    leave = Leave.objects.filter(user = user)

    context = {
        'user' : user,
        'profile' : employee,
        'leave_applications' : leave
    }

    return render(request, 'emp_dashboard/dashboard.html', context)


@login_required
def apply_for_leave(request):
    if request.method == 'POST':
        form = LeaveCreationForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Leave Request Sent. Wait for Admin\'s response.', extra_tags='alert alert-success alert-dismissible show')
            return redirect('emp_dashboard:dashboard')
        else:
            messages.error(request, 'Failed to request leave. Please check the entry dates and other details.', extra_tags='alert alert-warning alert-dismissible show')

    else:
        form = LeaveCreationForm()

    return render(request, 'emp_dashboard/apply_for_leave.html', {'form': form})
