# Generated by Django 2.0.5 on 2018-07-20 11:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0004_auto_20180720_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulepost',
            name='upvoted',
            field=models.ManyToManyField(related_name='user_votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
