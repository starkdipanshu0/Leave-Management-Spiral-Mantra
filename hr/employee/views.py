from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee
from .forms import EmployeeCreateForm
# Create your views here.

@login_required
def details(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employee/details.html', {'employee': employee})

@login_required
def profile_card(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employee_profile_card.html', {'employee': employee})

@login_required
def edit(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    # Ensure that only the user who owns the profile can edit it
    if request.user != employee.user:
        messages.error(request, "You are not authorized to edit this profile.")
        return redirect('employee_detail', employee_id=employee.id)

    if request.method == 'POST':
        form = EmployeeCreateForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee details updated successfully.')
            return redirect('employee_detail', employee_id=employee.id)
    else:
        form = EmployeeCreateForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})
