# Generated by Django 4.0.3 on 2022-05-29 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 6, 54, 32, 821628)),
        ),
    ]