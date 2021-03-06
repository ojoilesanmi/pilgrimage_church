# Generated by Django 3.1.2 on 2021-03-07 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilgrimage_app', '0004_auto_20201015_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(max_length=256)),
                ('cloudinary_link', models.URLField(max_length=256)),
                ('date_released', models.DateTimeField(default=datetime.datetime.now)),
                ('message_image', models.URLField(max_length=256)),
            ],
        ),
    ]
