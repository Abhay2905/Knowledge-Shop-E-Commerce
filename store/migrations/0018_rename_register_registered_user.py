# Generated by Django 5.0.3 on 2024-04-05 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_remove_register_confirm_passwod'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Registered_user',
        ),
    ]