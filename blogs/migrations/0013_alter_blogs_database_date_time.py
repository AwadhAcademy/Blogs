# Generated by Django 4.0.3 on 2022-05-29 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_alter_blogs_database_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs_database',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 6, 54, 32, 827264)),
        ),
    ]
