# Generated by Django 4.0.10 on 2024-11-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
