# Generated by Django 5.0.3 on 2024-10-02 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunch', '0005_remove_cours_course_oppos_remove_cours_course_road_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='course_field',
            field=models.CharField(choices=[('WD', 'web development'), ('AD', 'App development'), ('ML', 'Machine learning'), ('AI', 'Artificial intelligence'), ('DS', 'Data science'), ('CS', 'Cyber security')], default=0, max_length=2),
        ),
    ]
