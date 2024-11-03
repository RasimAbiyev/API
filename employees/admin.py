from django.contrib import admin
from .models import Department, Position, Employee, User, BlackListedIPAddresses

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'department', 'created_at')
    search_fields = ('name', 'department__name')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'department', 'position', 'status')
    search_fields = ('name', 'surname', 'department__name', 'position__name')

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email')

@admin.register(BlackListedIPAddresses)
class BlackListedIPAddressesAdmin(admin.ModelAdmin):
    list_display = ('ip_address',)
    search_fields = ('ip_address',)