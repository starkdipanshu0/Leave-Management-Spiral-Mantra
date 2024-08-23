from django.urls import path
from . import views

app_name = 'employee'
urlpatterns = [

    path('<int:employee_id>/', views.details, name='details'),
    path('<int:employee_id>/profile/', views.profile_card, name='profile_card'),
    path('<int:employee_id>/edit/', views.edit, name='edit'),
]
