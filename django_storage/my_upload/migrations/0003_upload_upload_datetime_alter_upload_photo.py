# Generated by Django 4.1 on 2022-09-03 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_upload', '0002_remove_upload_id_remove_upload_name_upload_photo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='upload_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='upload',
            name='photo',
            field=models.ImageField(upload_to='2022-09-03/'),
        ),
    ]
