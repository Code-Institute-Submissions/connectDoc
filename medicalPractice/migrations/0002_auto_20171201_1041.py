# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medicalPractice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalPractice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('address', models.TextField(default='', max_length=254)),
                ('position', geoposition.fields.GeopositionField(blank=True, max_length=42)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='location',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='position',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='practice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalPractice.MedicalPractice'),
        ),
    ]
