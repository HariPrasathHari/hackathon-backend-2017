from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.conf import settings
from app.models import Post
# from Status.models import StatusOfSchemes
from django.utils.safestring import mark_safe
from markdown_deux import markdown


# Create your models here.
class AppliedSchemes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    scheme = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False)
    date_applied = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.scheme.slug+' : '+self.user.username+' : '+str(self.date_applied)


# def create_user(instance, new_user=None):
#     if new_user is None:
#         new_user = instance.request.user
#         user = new_user
#     return user
#
#
# def pre_save_AppliedSchemes_receiver(sender, instance, *args, **kwargs):
#     if not instance.user:
#         instance.user = create_user(instance)
#     StatusOfSchemes.objects.create(scheme_id=instance)
#
#
#
#
#
# pre_save.connect(pre_save_AppliedSchemes_receiver, sender=AppliedSchemes)
