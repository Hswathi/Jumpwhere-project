# Generated by Django 4.1.7 on 2023-05-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0014_remove_employee_eamil_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
