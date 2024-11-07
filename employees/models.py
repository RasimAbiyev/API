from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission

class Department(models.Model):
    name = models.CharField(_('Department Name'), max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the department name."""
        return self.name

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

class Position(models.Model):
    name = models.CharField(_('Position Name'), max_length=100)
    salary = models.DecimalField(_('Salary'), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Position")
        verbose_name_plural = _("Positions")

class Employee(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    surname = models.CharField(_('Surname'), max_length=255)
    email = models.EmailField(_('Email'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.CASCADE)
    position = models.ForeignKey(Position, verbose_name=_("Position"), on_delete=models.CASCADE)
    status = models.CharField(_('Status'), max_length=50)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', _('Admin')),
        ('user', _('User')),
    )
    role = models.CharField(_('Role'), max_length=10, choices=ROLE_CHOICES, default='user')

    groups = models.ManyToManyField(
        Group,
        related_name='employees_user_groups',
        blank=True,
        verbose_name=_("Groups")
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='employees_user_permissions',
        blank=True,
        verbose_name=_("User Permissions")
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

class BlackListedIPAddresses(models.Model):
    ip_address = models.GenericIPAddressField(_('IP Address'))

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name = _('Black Listed IP Address')
        verbose_name_plural = _('Black Listed IP Addresses')