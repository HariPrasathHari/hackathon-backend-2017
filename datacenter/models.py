from django.db import models

# Create your models here.


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
    Landmark = models.CharField(max_length=10)
    Village_ot_town_or_city = models.CharField(max_length=10)
    District = models.CharField(max_length=10)
    State = models.CharField(max_length=15)
    Nationality = models.CharField(max_length=15)
    Pincode = models.CharField(max_length=6)
    Email = models.EmailField()
    Mobile_no = models.IntegerField()
    Nationality = models.CharField(max_length=15)
    bank = models.CharField(max_length=20)
    Account_no = models.CharField(max_length=18)
    bank_name = models.CharField(max_length=30)
    Branch_code = models.IntegerField()
    IFSC_code = models.IntegerField()
    MICR = models.IntegerField()
    house_or_building_or_apartment_no = models.CharField(max_length=10)
    Landmark = models.CharField(max_length=10)
    Village_ot_town_or_city = models.CharField(max_length=10)
    District = models.CharField(max_length=10)
    State = models.CharField(max_length=15)
    Nationality = models.CharField(max_length=15)
    Pincode = models.CharField(max_length=6)


class BGateway_database(models.Model):
    Aadhar_no = models.OneToOneField(aadhar_Database)
    Account_no = models.CharField(max_length=18)
    name = models.CharField(max_length=30)
    Branch_code = models.IntegerField()
    IFSC_code = models.IntegerField()
    MICR = models.IntegerField()
    house_or_building_or_apartment_no = models.CharField(max_length=10)
    Landmark = models.CharField(max_length=10)
    Village_ot_town_or_city = models.CharField(max_length=10)
    District = models.CharField(max_length=10)
    State = models.CharField(max_length=15)
    Nationality = models.CharField(max_length=15)
    Pincode = models.CharField(max_length=6)
    Phone_no = models.IntegerField()


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
    name = models.CharField(
        max_length=30,
        choices=unit_types,
    )
    name_of_the_office = models.CharField(max_length=20)
    dob = models.DateField()


class Employment(models.Model):
    Aadhar_no = models.OneToOneField(aadhar_Database)
    name = models.CharField(max_length=30)
    house_or_building_or_apartment_no = models.CharField(max_length=10)
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


class Income_database(models.Model):
    Name = models.OneToOneField(max_length=10)
    Aadhar_no = models.OneToOneField(aadhar_Database)
    Father_or_Husband_Name = models.CharField(max_length=10)

    Gender_choices = (
        ('Male', 'male'),
        ('female', 'female')
    )
    Gender = models.CharField(max_length=10,
                              choices=Gender_choices,
                              )
    house_or_building_or_apartment_no = models.CharField(max_length=10)
    Landmark = models.CharField(max_length=10)
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
    Landmark = models.CharField(max_length=50)
    Village_ot_town_or_city = models.CharField(max_length=50)
    District = models.CharField(max_length=20)
    State = models.CharField(max_length=15)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    Father_occupation = models.CharField(max_length=30)
    mother_occupation = models.CharField(max_length=30)


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


class Ration_Card(models.Model):
    Ration_Card_number = models.IntegerField()
    Aadhar_no = models.OneToOneField(aadhar_Database)
    Taluk = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Father_Name_or_Husband_choices = (
                                        ('Father','father'),
                                      ('husband','husband'))
    Father_or_Husband = models.CharField(max_length=9,
                                          choices=Father_Name_or_Husband_choices
                                          )
    Father_Name_or_Husband = models.CharField(max_length=30)
    house_or_building_or_apartment_no = models.CharField(max_length=10)
    Landmark = models.CharField(max_length=20)
    Village_ot_town_or_city = models.CharField(max_length=20)
    District = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Nationality = models.CharField(max_length=15)
    Pincode = models.CharField(max_length=6)
    Telephone = models.IntegerField()
    Mobile = models.IntegerField()
    Family = models.ManyToManyField(Ration_card_er)

class College(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    aicte_code = models.CharField(max_length=12)


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
    Landmark = models.CharField(max_length=10)
    Village_ot_town_or_city = models.CharField(max_length=10)
    District = models.CharField(max_length=10)
    State = models.CharField(max_length=15)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    Father_occupation = models.CharField(max_length=30)
    mother_occupation = models.CharField(max_length=30)
    college_id = models.ForeignKey(College)
