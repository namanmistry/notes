# Generated by Django 3.1.7 on 2021-04-16 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20210413_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='date_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 4, 16, 16, 8, 15, 916761)),
        ),
    ]
