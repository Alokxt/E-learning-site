# Generated by Django 5.0.3 on 2024-11-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopp', '0008_alter_shopsy_item_prize'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopsy',
            name='prize',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shopsy',
            name='item_prize',
            field=models.IntegerField(default=0),
        ),
    ]
