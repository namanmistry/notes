# Generated by Django 3.1.7 on 2021-04-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=300)),
                ('paragraph', models.CharField(max_length=10000)),
            ],
        ),
    ]
