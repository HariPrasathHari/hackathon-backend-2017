from django.db import models


# Create your models here.
# asd

class aadhar_Database(models.Model):
    name = models.CharField(max_length=30)
    Gender_choices = (
        ('Male', 'male'),
        ('female', 'female')
    )
    Gender = models.CharField(max_length=10,
                              choices=Gender_choices,
                              )
    dob = models.DateField()
    house_or_building_or_apartment_no = models.CharField(max_length=10)
    Landmark = models.CharField(max_length=50)
    Village_ot_town_or_city = models.CharField(max_length=10)
    District = models.CharField(max_length=10)
    State = models.CharField(max_length=15)
    Nationality = models.CharField(max_length=15)
    Pincode = models.CharField(max_length=6)
    Email = models.EmailField()
    Mobile_no = models.BigIntegerField()
    bank = models.CharField(max_length=20)
    Account_no = models.CharField(max_length=18)
    bank_name = models.CharField(max_length=30)
    Branch_code = models.IntegerField()
    IFSC_code = models.IntegerField()
    MICR = models.IntegerField()

    def __str__(self):
        return str(self.name)



class BGateway_database(models.Model):
    Aadhar_no = models.OneToOneField(aadhar_Database)
    Account_no = models.CharField(max_length=18)
    name = models.CharField(max_length=30)
    Branch_code = models.IntegerField()
    IFSC_code = models.IntegerField()
    MICR = models.IntegerField()
    house_or_building_or_apartment_no = models.CharField(max_length=100)
    Landmark = models.CharField(max_length=10)
    Village_ot_town_or_city = models.CharField(max_length=10)
    District = models.CharField(max_length=10)
    State = models.CharField(max_length=15)
    Nationality = models.CharField(max_length=15)
    Pincode = models.CharField(max_length=6)
    Phone_no = models.IntegerField()

    def __str__(self):
        return str(self.name)


class HealthInsuranceDatabase(models.Model):
    Aadhar_no = models.OneToOneField(aadhar_Database)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    unit_types = (
        ('Govt', 'govt'),
        ('public', 'public'),
        ('private', 'private'),
        ('other', 'other'),
    )
    type = models.CharField(
        max_length=30,
        choices=unit_types,
    )
    name_of_the_office = models.CharField(max_length=20)
    dob = models.DateField()

    def __str__(self):
        return str(self.name)


class Employment(models.Model):
    Aadhar_no = models.OneToOneField(aadhar_Database)
    name = models.CharField(max_length=30)
    house_or_building_or_apartment_no = models.CharField(max_length=100)
    Landmark = models.CharField(max_length=10)
    Village_ot_town_or_city = models.CharField(max_length=10)
    District = models.CharField(max_length=10)
    State = models.CharField(max_length=15)
    Nationality = models.CharField(max_length=15)
    SSN = models.CharField(max_length=12)
    Telephone_no = models.IntegerField()
    unit_types = (
        ('10th', '10Th'),
        ('12th', '12th'),
        ('P.G', 'P.G'),
        ('U.G', 'U.G'),
        ('MBA', 'MBA'),
    )
    Educational_Qualification = models.CharField(
        max_length=30,
        choices=unit_types,
    )
    community = models.CharField(max_length=4)
    Designation = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)


class Physically_Challenged(models.Model):
    Aadhar_no = models.OneToOneField(aadhar_Database)
    name = models.CharField(max_length=30)
    Type_of_disabilty = models.CharField(max_length=30)
    dob = models.DateField()
    unit_types = (
        ('10th', '10Th'),
        ('12th', '12th'),
        ('P.G', 'P.G'),
        ('U.G', 'U.G'),
        ('MBA', 'MBA'),
    )
    Educational_Qualification = models.CharField(
        max_length=30,
        choices=unit_types,
    )

    def __str__(self):
        return str(self.name)


class Income_database(models.Model):
    Name = models.CharField(max_length=10)
    Aadhar_no = models.OneToOneField(aadhar_Database)
    Father_Name_or_Husband_choices = (
        ('Father', 'father'),
        ('husband', 'husband'))
    Father_or_Husband = models.CharField(max_length=9,
                                         choices=Father_Name_or_Husband_choices
                                         )
    Father_or_Husband_name = models.CharField(max_length=30)
    Gender_choices = (
        ('Male', 'male'),
        ('female', 'female')
    )
    Gender = models.CharField(max_length=10,
                              choices=Gender_choices,
                              )
    house_or_building_or_apartment_no = models.CharField(max_length=10)
    Landmark = models.CharField(max_length=100)
    Village_ot_town_or_city = models.CharField(max_length=10)
    District = models.CharField(max_length=10)
    State = models.CharField(max_length=15)
    Nationality = models.CharField(max_length=15)
    Pincode = models.CharField(max_length=6)
    Monthly_income = models.IntegerField()
    Ration_card_number = models.CharField(max_length=12)
    Income_Tax = models.IntegerField()
    PAN_number = models.IntegerField()
    Bank_Account = models.ForeignKey(BGateway_database)

    def __str__(self):
        return str(self.Name)


class Student_db(models.Model):
    name = models.CharField(max_length=30)
    Aadhar_no = models.OneToOneField(aadhar_Database)
    dob = models.DateField()
    Gender_choices = (
        ('Male', 'male'),
        ('female', 'female')
    )
    Gender = models.CharField(max_length=10,
                              choices=Gender_choices,
                              )
    Nationality = models.CharField(max_length=15)
    Community = models.CharField(max_length=5)
    house_or_building_or_apartment_no = models.CharField(max_length=10)
    Landmark = models.CharField(max_length=100)
    Village_ot_town_or_city = models.CharField(max_length=50)
    District = models.CharField(max_length=20)
    State = models.CharField(max_length=15)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    Father_occupation = models.CharField(max_length=30)
    mother_occupation = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Ration_card_er(models.Model):
    name = models.CharField(max_length=30)
    Aadhar_no = models.OneToOneField(aadhar_Database)
    age = models.IntegerField()
    dob = models.DateField()
    Relation_choices = (('father', 'father'),
                        ('mother', 'mother'),
                        ('Husband', 'Husband'),
                        ('wife', 'wife'),
                        ('brother', 'brother'),
                        ('sister', 'sister'),
                        )
    Relation = models.CharField(max_length=10,
                                choices=Relation_choices
                                )

    def __str__(self):
        return str(self.name)


class Ration_Card(models.Model):
    Ration_Card_number = models.IntegerField()
    Aadhar_no = models.OneToOneField(aadhar_Database)
    Taluk = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Father_Name_or_Husband_choices = (
        ('Father', 'father'),
        ('husband', 'husband'))
    Father_or_Husband = models.CharField(max_length=9,
                                         choices=Father_Name_or_Husband_choices
                                         )
    Father_or_Husband_name = models.CharField(max_length=30)
    house_or_building_or_apartment_no = models.CharField(max_length=10)
    Landmark = models.CharField(max_length=100)
    Village_ot_town_or_city = models.CharField(max_length=20)
    District = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Nationality = models.CharField(max_length=15)
    Pincode = models.CharField(max_length=6)
    Telephone = models.IntegerField()
    Mobile = models.BigIntegerField()
    Family = models.ManyToManyField(Ration_card_er)

    def __str__(self):
        return str(self.Name)


class College(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    aicte_code = models.CharField(max_length=12)

    def __str__(self):
        return str(self.name)


class College_db(models.Model):
    name = models.CharField(max_length=30)
    Aadhar_no = models.OneToOneField(aadhar_Database)
    dob = models.DateField()
    duration_start = models.DateField()
    duration_end = models.DateField()
    Gender_choices = (
        ('Male', 'male'),
        ('female', 'female')
    )
    Gender = models.CharField(max_length=10,
                              choices=Gender_choices,
                              )
    Nationality = models.CharField(max_length=15)
    Community = models.CharField(max_length=5)
    house_or_building_or_apartment_no = models.CharField(max_length=10)
    Landmark = models.CharField(max_length=100)
    Village_ot_town_or_city = models.CharField(max_length=10)
    District = models.CharField(max_length=10)
    State = models.CharField(max_length=15)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    Father_occupation = models.CharField(max_length=30)
    mother_occupation = models.CharField(max_length=30)
    college_id = models.ForeignKey(College)

    def __str__(self):
        return str(self.name)


'''
from datacenter.models import *
qs=aadhar_Database.objects.all()


123456789012

from datacenter.models import *
obj_instance=aadhar_Database.objects.get(bank=123456789012)




'''