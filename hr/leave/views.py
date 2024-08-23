from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Leave
from leave.forms import LeaveCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def delete_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)

    if request.method == 'POST':
        leave.delete()
        messages.success(request, 'Leave request deleted successfully!')
        return redirect('emp_dashboard:leave_history')  # Redirect to a page showing the leave history or list
    return render(request, 'leave/confirm_delete.html', {'leave': leave})


@login_required
def approve_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)

    if request.user.is_staff:
        leave.approve_leave()
        messages.success(request, 'Leave approved successfully.')

        # Send email notification to the employee
        # subject = 'Your Leave Application Has Been Approved'
        # message = f'Dear {leave.user.get_full_name},\n\nYour leave application from {leave.startdate} to {leave.enddate} has been approved.\n\nBest regards,\nHR Team'
        # recipient_list = [leave.user.email]
        # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

    else:
        messages.error(request, 'You are not authorized to approve this leave.')

    return redirect(request.META.get('HTTP_REFERER', 'Admin:leave_application'))

@login_required
def reject_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)

    if request.user.is_staff:
        leave.reject_leave()
        messages.success(request, 'Leave rejected successfully.')

         # Send email notification to the employee
        # subject = 'Your Leave Application Has Been Rejected'
        # message = f'Dear {leave.employee.user.get_full_name},\n\nYour leave application from {leave.startdate} to {leave.enddate} has been rejected.\n\nBest regards,\nHR Team'
        # recipient_list = [leave.employee.user.email]
        # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

    else:
        messages.error(request, 'YoSu are not authorized to reject this leave.')

    return redirect(request.META.get('HTTP_REFERER', 'Admin:leave_application'))

@login_required
def cancel_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)

    if leave.user == request.user:
        leave.leaves_cancel()
        messages.success(request, 'Leave canceled successfully.')
    else:
        messages.error(request, 'You are not authorized to cancel this leave.')

    return redirect(request.META.get('HTTP_REFERER', 'emp_dashboard:leave_history'))

@login_required
def edit_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)

    if leave.user != request.user:
        messages.error(request, 'You are not authorized to edit this leave.')
        return redirect('emp_dashboard:leave_history')

    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            messages.success(request, 'Leave updated successfully.')
            return redirect('emp_dashboard:leave_history')
        else:
            messages.error(request, 'There was an error updating the leave.')
    else:
        form = LeaveForm(instance=leave)

    return render(request, 'leave/edit_leave.html', {'form': form})
