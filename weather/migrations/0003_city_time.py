# Generated by Django 3.0.2 on 2020-03-23 08:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20200311_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 8, 49, 52, 141941, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
