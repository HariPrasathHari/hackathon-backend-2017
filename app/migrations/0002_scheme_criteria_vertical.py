# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme_criteria_vertical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MIN_AGE', models.IntegerField()),
                ('MAX_AGE', models.IntegerField()),
                ('BANK_ACC_NO', models.BooleanField()),
                ('EDUCATIONAL_QUALIFICATION', models.CharField(max_length=30)),
                ('IS_INDIAN', models.BooleanField()),
                ('SAVINGS_ACC', models.BooleanField()),
                ('MAX_NO_OF_GIRL_CHILDREN', models.IntegerField()),
                ('MAX_NO_OF_CHILDREN', models.IntegerField()),
                ('Gender', models.CharField(choices=[('Male', 'male'), ('female', 'female')], max_length=10)),
                ('CASTE', models.CharField(max_length=20)),
                ('MARITAL_STATUS', models.BooleanField()),
                ('MIN_SALARY', models.IntegerField()),
                ('MAX_SALARY', models.IntegerField()),
                ('PREGNANT', models.BooleanField()),
                ('FARMER', models.BooleanField()),
                ('NO_OF_WORKING_YEARS', models.IntegerField()),
                ('MARKS_PERCENT', models.IntegerField()),
                ('EXCELLED_IN_ANY_SPOT', models.TextField()),
                ('EMPLOYED', models.BooleanField()),
                ('DISABLED', models.BooleanField()),
                ('IS_ENTREPRENEUR', models.BooleanField()),
            ],
        ),
    ]
