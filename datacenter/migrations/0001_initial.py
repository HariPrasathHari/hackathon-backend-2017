# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-19 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aadhar_Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Gender', models.CharField(choices=[(b'Male', b'male'), (b'female', b'female')], max_length=10)),
                ('dob', models.DateField()),
                ('house_or_building_or_apartment_no', models.CharField(max_length=10)),
                ('Landmark', models.CharField(max_length=50)),
                ('Village_ot_town_or_city', models.CharField(max_length=10)),
                ('District', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=15)),
                ('Nationality', models.CharField(max_length=15)),
                ('Pincode', models.CharField(max_length=6)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile_no', models.BigIntegerField()),
                ('bank', models.CharField(max_length=20)),
                ('Account_no', models.CharField(max_length=18)),
                ('bank_name', models.CharField(max_length=30)),
                ('Branch_code', models.IntegerField()),
                ('IFSC_code', models.IntegerField()),
                ('MICR', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BGateway_database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_no', models.CharField(max_length=18)),
                ('name', models.CharField(max_length=30)),
                ('Branch_code', models.IntegerField()),
                ('IFSC_code', models.IntegerField()),
                ('MICR', models.IntegerField()),
                ('house_or_building_or_apartment_no', models.CharField(max_length=100)),
                ('Landmark', models.CharField(max_length=10)),
                ('Village_ot_town_or_city', models.CharField(max_length=10)),
                ('District', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=15)),
                ('Nationality', models.CharField(max_length=15)),
                ('Pincode', models.CharField(max_length=6)),
                ('Phone_no', models.IntegerField()),
                ('Aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datacenter.aadhar_Database')),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('aicte_code', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='College_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('duration_start', models.DateField()),
                ('duration_end', models.DateField()),
                ('Gender', models.CharField(choices=[(b'Male', b'male'), (b'female', b'female')], max_length=10)),
                ('Nationality', models.CharField(max_length=15)),
                ('Community', models.CharField(max_length=5)),
                ('house_or_building_or_apartment_no', models.CharField(max_length=10)),
                ('Landmark', models.CharField(max_length=100)),
                ('Village_ot_town_or_city', models.CharField(max_length=10)),
                ('District', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=15)),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('Father_occupation', models.CharField(max_length=30)),
                ('mother_occupation', models.CharField(max_length=30)),
                ('Aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datacenter.aadhar_Database')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacenter.College')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('house_or_building_or_apartment_no', models.CharField(max_length=100)),
                ('Landmark', models.CharField(max_length=10)),
                ('Village_ot_town_or_city', models.CharField(max_length=10)),
                ('District', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=15)),
                ('Nationality', models.CharField(max_length=15)),
                ('SSN', models.CharField(max_length=12)),
                ('Telephone_no', models.IntegerField()),
                ('Educational_Qualification', models.CharField(choices=[(b'10th', b'10Th'), (b'12th', b'12th'), (b'P.G', b'P.G'), (b'U.G', b'U.G'), (b'MBA', b'MBA')], max_length=30)),
                ('community', models.CharField(max_length=4)),
                ('Designation', models.CharField(max_length=10)),
                ('Aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datacenter.aadhar_Database')),
            ],
        ),
        migrations.CreateModel(
            name='HealthInsuranceDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[(b'Govt', b'govt'), (b'public', b'public'), (b'private', b'private'), (b'other', b'other')], max_length=30)),
                ('name_of_the_office', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('Aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datacenter.aadhar_Database')),
            ],
        ),
        migrations.CreateModel(
            name='Income_database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Father_or_Husband', models.CharField(choices=[(b'Father', b'father'), (b'husband', b'husband')], max_length=9)),
                ('Father_or_Husband_name', models.CharField(max_length=30)),
                ('Gender', models.CharField(choices=[(b'Male', b'male'), (b'female', b'female')], max_length=10)),
                ('house_or_building_or_apartment_no', models.CharField(max_length=10)),
                ('Landmark', models.CharField(max_length=100)),
                ('Village_ot_town_or_city', models.CharField(max_length=10)),
                ('District', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=15)),
                ('Nationality', models.CharField(max_length=15)),
                ('Pincode', models.CharField(max_length=6)),
                ('Monthly_income', models.IntegerField()),
                ('Ration_card_number', models.CharField(max_length=12)),
                ('Income_Tax', models.IntegerField()),
                ('PAN_number', models.IntegerField()),
                ('Aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datacenter.aadhar_Database')),
                ('Bank_Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacenter.BGateway_database')),
            ],
        ),
        migrations.CreateModel(
            name='Physically_Challenged',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Type_of_disabilty', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('Educational_Qualification', models.CharField(choices=[(b'10th', b'10Th'), (b'12th', b'12th'), (b'P.G', b'P.G'), (b'U.G', b'U.G'), (b'MBA', b'MBA')], max_length=30)),
                ('Aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datacenter.aadhar_Database')),
            ],
        ),
        migrations.CreateModel(
            name='Ration_Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ration_Card_number', models.IntegerField()),
                ('Taluk', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=30)),
                ('Father_or_Husband', models.CharField(choices=[(b'Father', b'father'), (b'husband', b'husband')], max_length=9)),
                ('Father_or_Husband_name', models.CharField(max_length=30)),
                ('house_or_building_or_apartment_no', models.CharField(max_length=10)),
                ('Landmark', models.CharField(max_length=100)),
                ('Village_ot_town_or_city', models.CharField(max_length=20)),
                ('District', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('Nationality', models.CharField(max_length=15)),
                ('Pincode', models.CharField(max_length=6)),
                ('Telephone', models.IntegerField()),
                ('Mobile', models.BigIntegerField()),
                ('Aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datacenter.aadhar_Database')),
            ],
        ),
        migrations.CreateModel(
            name='Ration_card_er',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('Relation', models.CharField(choices=[(b'father', b'father'), (b'mother', b'mother'), (b'Husband', b'Husband'), (b'wife', b'wife'), (b'brother', b'brother'), (b'sister', b'sister')], max_length=10)),
                ('Aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datacenter.aadhar_Database')),
            ],
        ),
        migrations.CreateModel(
            name='Student_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('Gender', models.CharField(choices=[(b'Male', b'male'), (b'female', b'female')], max_length=10)),
                ('Nationality', models.CharField(max_length=15)),
                ('Community', models.CharField(max_length=5)),
                ('house_or_building_or_apartment_no', models.CharField(max_length=10)),
                ('Landmark', models.CharField(max_length=100)),
                ('Village_ot_town_or_city', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=15)),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('Father_occupation', models.CharField(max_length=30)),
                ('mother_occupation', models.CharField(max_length=30)),
                ('Aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datacenter.aadhar_Database')),
            ],
        ),
        migrations.AddField(
            model_name='ration_card',
            name='Family',
            field=models.ManyToManyField(to='datacenter.Ration_card_er'),
        ),
    ]
