# Generated by Django 3.1.7 on 2021-03-15 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_feed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResetAuth',
        ),
    ]
