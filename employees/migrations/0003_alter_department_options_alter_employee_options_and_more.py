# Generated by Django 4.0.10 on 2024-11-02 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employees', '0002_blacklistedipaddresses'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Department', 'verbose_name_plural': 'Departments'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Position', 'verbose_name_plural': 'Positions'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='blacklistedipaddresses',
            name='ip_address',
            field=models.GenericIPAddressField(verbose_name='IP Address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.position', verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(max_length=255, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='position',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='position',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salary'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='employees_user_groups', to='auth.group', verbose_name='Groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=10, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='employees_user_permissions', to='auth.permission', verbose_name='User Permissions'),
        ),
    ]
