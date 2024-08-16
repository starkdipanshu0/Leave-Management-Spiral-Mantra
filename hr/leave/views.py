from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Leave
# Create your views here.
def delete_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)

    if request.method == 'POST':
        leave.delete()
        messages.success(request, 'Leave request deleted successfully!')
        return redirect('leave_history')  # Redirect to a page showing the leave history or list
    return render(request, 'confirm_delete.html', {'leave': leave})

def edit_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)

    if request.method == 'POST':
        form = LeaveCreationForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            messages.success(request, 'Leave request updated successfully!')
            return redirect('emp_dashboard:leave_history')  # Adjust the redirect as needed
    else:
        form = LeaveCreationForm(instance=leave)

    return render(request, 'edit_leave.html', {'form': form, 'leave': leave})
