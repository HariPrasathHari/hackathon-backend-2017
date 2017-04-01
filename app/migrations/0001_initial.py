# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate_Proof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_id', models.TextField(null=True)),
                ('title', models.CharField(max_length=30)),
                ('launch_date', models.DateField()),
                ('is_active', models.BooleanField()),
                ('slug', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Scheme_criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MIN_AGE', 'MIN_AGE'), ('MAX_AGE', 'MAX_AGE'), ('BANK_ACC_NO', 'BANK_ACC_NO'), ('EDUCATIONAL_QUALIFICATION', 'EDUCATIONAL_QUALIFICATION'), ('NATIONALITY', 'NATIONALITY'), ('SAVINGS_ACC', 'SAVINGS_ACC'), ('MAX_NO_OF_GIRL_CHILDREN', 'MAX_NO_OF_GIRL_CHILDREN'), ('MAX_NO_OF_CHILDREN', 'MAX_NO_OF_CHILDREN'), ('GENDER', 'GENDER'), ('CASTE', 'CASTE'), ('MARITAL_STATUS', 'MARITAL_STATUS'), ('MIN_SALARY', 'MIN_SALARY'), ('PREGNANT', 'PREGNANT'), ('FARMER', 'FARMER'), ('NO_OF_WORKING_YEARS', 'NO_OF_WORKING_YEARS'), ('NO_OF_WORKING_YEARS', 'NO_OF_WORKING_YEARS'), ('EXCELLED_IN_ANY_SPOT', 'EXCELLED_IN_ANY_SPOT'), ('EMPLOYED', 'EMPLOYED'), ('DISABLED', 'DISABLED')], max_length=30)),
                ('type', models.CharField(choices=[('NUMERIC', 'NUMERIC'), ('LIST', 'LIST'), ('BOOLEAN', 'BOOLEAN')], max_length=10)),
                ('Required_field', models.TextField()),
                ('Required_documents', models.ManyToManyField(to='app.Certificate_Proof')),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Post')),
            ],
        ),
    ]
