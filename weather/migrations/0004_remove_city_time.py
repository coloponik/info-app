# Generated by Django 3.0.2 on 2020-03-23 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_city_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='time',
        ),
    ]
