# Generated by Django 3.1.7 on 2021-03-16 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20210315_2057'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feed',
            new_name='Site',
        ),
    ]
