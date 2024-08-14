from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
# class EducationInline(admin.TabularInline):
#     model = Education
#     can_delete = False
#     verbose_name_plural = 'Education'
#     fk_name = 'employee'  # This specifies the foreign key relationship

# class EmployeeAdmin(admin.ModelAdmin):
#     inlines = [EducationInline]
#     list_display = ('name',)
#     search_fields = ('name',)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Optionally specify which fields to display in the admin list view and forms
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'user_type', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register the CustomUser model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Employee)

admin.site.register(Education)

