from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('email', 'first_name', 'last_name', 'contact_no', 'is_active', 'is_staff')
    
    # Fields to filter in the admin list view
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    
    # Fields to use for searching
    search_fields = ('email', 'first_name', 'last_name', 'contact_no')
    
    # Fieldsets for organizing the form layout
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'contact_no')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('OTP Info', {
            'fields': ('otp', 'otp_expiry')
        }),
        ('Important Dates', {
            'fields': ('last_login',)
        }),
    )
    
    # Fields to use for creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'contact_no', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )
    
    # The model's primary field used for identification
    ordering = ('email',)

# Register the CustomUser model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
