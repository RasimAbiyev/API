# Generated by Django 4.0.10 on 2024-11-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackListedIPAddresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
            ],
            options={
                'verbose_name': 'Black Listed IP Address',
                'verbose_name_plural': 'Black Listed IP Addresses',
            },
        ),
    ]
