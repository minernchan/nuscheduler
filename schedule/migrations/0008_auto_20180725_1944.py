# Generated by Django 2.0.5 on 2018-07-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20180724_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulepost',
            name='modules_taken',
            field=models.CharField(max_length=500),
        ),
    ]
