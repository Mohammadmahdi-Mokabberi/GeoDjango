# Generated by Django 4.0.4 on 2022-04-24 23:08

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incidences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Incidences',
            },
        ),
    ]
