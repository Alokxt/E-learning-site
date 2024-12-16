# Generated by Django 5.0.3 on 2024-10-18 03:06

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunch', '0008_rename_tasks_todo_user'),
        ('shopp', '0006_delete_user_profle'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('since_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.CharField(max_length=300)),
                ('orders', models.ManyToManyField(to='shopp.shopsy')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]