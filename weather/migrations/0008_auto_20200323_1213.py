# Generated by Django 3.0.2 on 2020-03-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0007_city_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]