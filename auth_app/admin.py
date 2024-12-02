from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin

# Customize the AdminSite class
class MyAdminSite(admin.AdminSite):
    site_header = "Adwik Works Admin"  # Header displayed on the top
    site_title = "ADWIK WORKS"   # Title shown in the browser's title bar
    index_title = "Welcome to the Adwik Works"  # Title displayed on the admin index page

# Register your custom AdminSite instance
admin.site = MyAdminSite()


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
