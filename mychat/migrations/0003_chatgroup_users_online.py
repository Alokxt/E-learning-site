# Generated by Django 5.1.2 on 2024-12-11 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunch', '0010_rename_user_profle_profile'),
        ('mychat', '0002_alter_groupmessage_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgroup',
            name='users_online',
            field=models.ManyToManyField(blank=True, related_name='users_online', to='bunch.profile'),
        ),
    ]
