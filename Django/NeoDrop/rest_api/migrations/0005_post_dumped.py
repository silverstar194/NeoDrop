# Generated by Django 2.0.2 on 2018-02-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_auto_20180225_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dumped',
            field=models.BooleanField(default=False),
        ),
    ]
