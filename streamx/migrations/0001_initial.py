# Generated by Django 5.1.2 on 2024-12-26 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bunch', '0010_rename_user_profle_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coursevideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(default='Untitiled-vd', max_length=250)),
                ('video_thumbnail', models.ImageField(blank=True, upload_to='media/')),
                ('video', models.FileField(upload_to='videos/')),
                ('video_description', models.TextField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bunch.cours')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Playlist_name', models.CharField(max_length=350)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bunch.cours')),
                ('video_list', models.ManyToManyField(to='streamx.coursevideos')),
            ],
        ),
    ]
