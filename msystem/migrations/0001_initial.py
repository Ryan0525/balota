# Generated by Django 4.0.4 on 2022-06-28 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.CharField(max_length=3)),
                ('Address', models.CharField(max_length=50)),
                ('Contact_No', models.CharField(max_length=20)),
                ('Emailaddress', models.CharField(max_length=30)),
                ('Company_id', models.CharField(max_length=10)),
                ('Gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Days', models.TextField(default='')),
                ('Rate', models.TextField(default='')),
                ('Deduction', models.TextField(default='')),
                ('Total', models.TextField(default='')),
                ('Date_time', models.DateTimeField(default='')),
                ('employee_info', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='msystem.employee_info')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employeereport', models.TextField(default='')),
                ('Employee_comment', models.TextField(default='')),
                ('Company_rating', models.TextField(default='')),
                ('Empreport_date', models.DateTimeField(default='')),
                ('employee_emrep', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='msystem.employee_info')),
            ],
        ),
        migrations.CreateModel(
            name='Company_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Companyreport', models.TextField(default='')),
                ('Company_comment', models.TextField(default='')),
                ('Comreport_date', models.DateTimeField(default='')),
                ('employee_comrep', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='msystem.employee_info')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_branch', models.CharField(choices=[('Cavite', 'cavite'), ('Manila', 'manila'), ('Caloocan', 'caloocan'), ('Taguig', 'taguig')], default='', max_length=20)),
                ('Department', models.CharField(choices=[('Operations', 'operations'), ('Quality Assurance', 'QA'), ('Human Resource', 'HR'), ('Administration', 'Admin'), ('Training', 'training')], default='', max_length=20)),
                ('Position', models.TextField(default='')),
                ('employee_branch', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='msystem.employee_info')),
            ],
        ),
    ]
