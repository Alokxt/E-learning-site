# Generated by Django 5.0.3 on 2024-10-19 23:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunch', '0010_rename_user_profle_profile'),
        ('social', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='follower_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=200)),
                ('profile_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bunch.profile')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
