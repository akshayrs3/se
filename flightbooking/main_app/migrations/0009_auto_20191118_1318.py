# Generated by Django 2.1.5 on 2019-11-18 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20191118_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.time(13, 18, 1, 689509)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 18, 13, 18, 1, 689446)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.time(13, 18, 1, 689472)),
        ),
    ]