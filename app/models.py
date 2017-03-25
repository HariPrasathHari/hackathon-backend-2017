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
    title=models.CharField(max_length=30)
    body=models.TextField()
    date=models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __str__(self):
        return self.title


    def __unicode__(self):
        return self.title

    def get_markdown(self):
        body = self.body
        markdown_text = markdown(body)
        return mark_safe(markdown_text)

    def get_absolute_url(self):
        return reverse("postss-api:list", kwargs={"title": self.title})

    def get_api_url(self):
        return reverse("postss-api:Detailedview", kwargs={"title": self.title})



def create_title(instance, new_slug=None):
    title = slugify(instance.body)
    if new_slug is not None:
        title = new_slug
    qs = Post.objects.filter(title=title).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(title, qs.first().id)
        return create_title(instance, new_slug=new_slug)
    return title


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.title:
        instance.title = create_title(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)

class schemes(models.Model):
    min_age=models.IntegerField()
    max_salaray=models.IntegerField()
    req_community=models.CharField(max_length=4)
    scheme_name=models.CharField(max_length=30)


    def __str__(self):
        return self.scheme_name
