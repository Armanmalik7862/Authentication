# Generated by Django 4.2.4 on 2023-08-30 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='First_Name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Last_Name',
            new_name='last_name',
        ),
    ]
