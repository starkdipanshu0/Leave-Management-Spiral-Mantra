from django.urls import path
from . import views

app_name = 'Admin'

urlpatterns = [
    path('leave_application/',views.leave_application,name='leave_application'),
    path('employee_list/',views.employee_list,name='employee_list'),
    # path('apply_for_leave/',views.apply_for_leave,name='apply_for_leave'),
    # path('leave_history/',views.leave_history,name='leave_history'),
    path('departments/', views.department_list, name='department_list'),
    path('department/<int:department_id>/', views.department_detail, name='department_detail'),

]

