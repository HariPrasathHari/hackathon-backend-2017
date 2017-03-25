from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.conf import settings
from django.utils.safestring import mark_safe
from markdown_deux import markdown

# Create your models here.

class Profiledet(models.Model):
    age=models.IntegerField()
    salaray=models.IntegerField()
    community=models.CharField(max_length=4)
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default=1)


    def __str__(self):
        return self.first_name