# Generated by Django 4.0.3 on 2022-05-28 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_loogin_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs_database',
            name='id',
        ),
        migrations.AddField(
            model_name='blogs_database',
            name='unique_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
