# Generated by Django 4.0.4 on 2022-06-29 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msystem', '0005_rename_muncipality_branch_municipality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='Municipality',
            new_name='Department',
        ),
    ]