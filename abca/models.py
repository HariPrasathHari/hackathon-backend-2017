from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# # Create your models here.
# class CustomUserManager(BaseUserManager):
#    def create_user(self, email, password=None, is_staff_account=None, activation_key=None, key_expires=None):
#        """
#        Creates and saves a User with the given email, date of
#        birth and password.
#        """
#        user = self.model(
#            email=self.normalize_email(email),
#            is_staff_account=is_staff_account,
#            activation_key=activation_key,
#            key_expires=key_expires
#        )
#
#        user.set_password(password)
#        user.save(using=self._db)
#        return user
#
#    def create_superuser(self, email, password, activation_key=None, key_expires=None):
#        """
#        Creates and saves a superuser with the given email, date of
#        birth and password.
#        """
#        user = self.create_user(
#            email,
#            password=password,
#            activation_key=activation_key,
#            key_expires=key_expires,
#            is_staff_account=True
#        )
#        user.is_approved = True
#        user.is_active = True
#        user.is_superuser = True
#        user.has_filled_data = True
#        user.save(using=self._db)
#        return user
#
#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#    aadhaar_number = models.CharField(
#        verbose_name='aadhaar number',
#        max_length=12,
#        unique=True,
#    )
#    is_staff_account = models.BooleanField(default=False)
#    is_active = models.BooleanField(default=True)
#    objects = CustomUserManager()
#    # history = HistoricalRecords()
#
#    USERNAME_FIELD = 'aadhaar_number'
#    REQUIRED_FIELDS = []
#
#    def get_full_name(self):
#        # The user is identified by their email address
#        return self.aadhaar_number
#
#    def get_short_name(self):
#        # The user is identified by their email address
#        return self.aadhaar_number
#
#    def __str__(self):  # __unicode__ on Python 2
#        return self.aadhaar_number
#
#    @property
#    def is_staff(self):
#        "Is the user a member of staff?"
#        # Simplest possible answer: All admins are staff
#        return self.is_superuser
#
