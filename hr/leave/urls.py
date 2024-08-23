from django.urls import path
from . import views
app_name = 'leave'
urlpatterns = [
    # Other URL patterns
    path('delete/<int:leave_id>/', views.delete_leave, name='delete_leave'),
    path('edit/<int:leave_id>/', views.edit_leave, name='edit_leave'),
    path('approve/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('reject/<int:leave_id>/', views.reject_leave, name='reject_leave'),
    path('cancel/<int:leave_id>/', views.cancel_leave, name='cancel_leave'),
]
