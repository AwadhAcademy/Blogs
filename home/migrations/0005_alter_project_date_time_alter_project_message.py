# Generated by Django 4.0.3 on 2022-05-29 06:59

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_project_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 6, 59, 9, 839206)),
        ),
        migrations.AlterField(
            model_name='project',
            name='message',
            field=tinymce.models.HTMLField(),
        ),
    ]
