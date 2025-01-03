# Generated by Django 5.0.3 on 2024-10-18 01:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopp', '0003_remove_cartitem_cart_cartitem_user_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('since_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.CharField(max_length=300)),
                ('orders', models.ManyToManyField(to='shopp.shopsy')),
            ],
        ),
    ]
