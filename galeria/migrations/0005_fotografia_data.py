# Generated by Django 5.1.1 on 2024-10-23 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_alter_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
