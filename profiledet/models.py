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
    age = models.IntegerField()
    salary = models.IntegerField()
    community = models.CharField(max_length=4)
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default=1)

    def __str__(self):
        return self.first_name


def create_user(instance, new_user=None):
    if new_user is None:
        new_user = instance.request.user
        user = new_user
    return user


def pre_save_profiledet_receiver(sender, instance, *args, **kwargs):
    if not instance.user:
        instance.user = create_user(instance)

pre_save.connect(pre_save_profiledet_receiver, sender=Profiledet)
