# Generated by Django 3.1.7 on 2021-04-27 02:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0004_auto_20210315_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='user_site_relation',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
