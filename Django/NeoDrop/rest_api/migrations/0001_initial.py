# Generated by Django 2.0.2 on 2018-02-25 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nano_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageUrl', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('isActive', models.BooleanField(default=True)),
                ('isFunded', models.BooleanField(default=False)),
                ('imageUrl', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('amazonLink', models.CharField(max_length=300)),
                ('organization', models.CharField(max_length=300)),
                ('person', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('plea', models.CharField(max_length=300)),
                ('raisedNano', models.IntegerField()),
                ('raisedUsd', models.FloatField()),
                ('priceNano', models.FloatField()),
                ('priceUsd', models.FloatField()),
                ('numDonations', models.FloatField()),
                ('timeLeft', models.IntegerField()),
            ],
        ),
    ]