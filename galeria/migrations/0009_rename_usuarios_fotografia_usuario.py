# Generated by Django 5.1.1 on 2024-10-29 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0008_fotografia_usuarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='usuarios',
            new_name='usuario',
        ),
    ]