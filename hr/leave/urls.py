from django.urls import path
from . import views
app_name = 'leave'
urlpatterns = [
    # Other URL patterns
    path('delete/<int:leave_id>/', views.delete_leave, name='delete_leave'),
    path('edit/<int:leave_id>/', views.edit_leave, name='edit_leave'),
]
