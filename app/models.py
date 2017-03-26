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
class  Post(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    min_age = models.IntegerField()
    max_salary = models.IntegerField()
    slug = models.CharField(max_length=30)
    req_community = models.CharField(max_length=4)

    def __str__(self):
        return self.title


    def __unicode__(self):
        return self.title

    def get_markdown(self):
        slug = self.slug
        markdown_text = markdown(slug)
        return mark_safe(markdown_text)

    def get_absolute_url(self):
        return reverse("postss-api:list", kwargs={"slug": self.slug})

    def get_api_url(self):
        return reverse("postss-api:DetailedView", kwargs={"slug": self.slug})



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

# def create_user(instance, new_user=None):
#     if new_user is None:
#         new_user = instance.request.user
#         user = new_user
#     return user

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)