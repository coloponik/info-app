# Generated by Django 3.0.2 on 2020-03-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_remove_city_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='time',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
