# Generated by Django 5.0.3 on 2024-10-18 20:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bunch', '0009_user_profle'),
        ('shopp', '0006_delete_user_profle'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_profle',
            new_name='Profile',
        ),
    ]