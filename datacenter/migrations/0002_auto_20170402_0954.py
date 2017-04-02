# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('datacenter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aadhar_database',
            name='Mobile_no',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='bgateway_database',
            name='house_or_building_or_apartment_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='college',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='college_db',
            name='Landmark',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employment',
            name='house_or_building_or_apartment_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='income_database',
            name='Landmark',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ration_card',
            name='Landmark',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ration_card',
            name='Mobile',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='student_db',
            name='Landmark',
            field=models.CharField(max_length=100),
        ),
    ]