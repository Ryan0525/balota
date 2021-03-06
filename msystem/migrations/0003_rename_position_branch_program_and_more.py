# Generated by Django 4.0.4 on 2022-06-29 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msystem', '0002_member_info_alter_branch_employee_branch_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='Position',
            new_name='Program',
        ),
        migrations.RenameField(
            model_name='employee_salary',
            old_name='Deduction',
            new_name='Offense',
        ),
        migrations.RenameField(
            model_name='employee_salary',
            old_name='employee_info',
            new_name='member_info',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='Department',
        ),
        migrations.AddField(
            model_name='branch',
            name='Muncipality',
            field=models.CharField(choices=[('Dasma', 'operations'), ('Trece', 'QA'), ('Binan', 'HR'), ('Pasay', 'Admin'), ('Lobo', 'training')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Company_branch',
            field=models.CharField(choices=[('Cavite', 'cavite'), ('Manila', 'manila'), ('Laguna', 'caloocan'), ('Batangas', 'taguig')], default='', max_length=20),
        ),
    ]
