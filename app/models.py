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

class Certificate_Proof(models.Model):
    document = models.FileField(upload_to='documents/')


class Documents(models.Model):
    doc = models.CharField(max_length=20)

    def __str__(self):
        return self.doc


class Scheme_criteria(models.Model):
    MIN_AGE = 'MIN_AGE'
    MAX_AGE = 'MAX_AGE'
    BANK_ACC_NO = 'BANK_ACC_NO'
    EDUCATIONAL_QUALIFICATION = 'EDUCATIONAL_QUALIFICATION'
    NATIONALITY = 'NATIONALITY'
    SAVINGS_ACC = 'SAVINGS_ACC'
    MAX_NO_OF_GIRL_CHILDREN = 'MAX_NO_OF_GIRL_CHILDREN'
    MAX_NO_OF_CHILDREN = 'MAX_NO_OF_CHILDREN'
    GENDER = 'GENDER'
    CASTE = 'CASTE'
    MARITAL_STATUS = 'MARITAL_STATUS'
    MIN_SALARY = 'MIN_SALARY'
    PREGNANT = 'PREGNANT'
    FARMER = 'FARMER'
    NO_OF_WORKING_YEARS = 'NO_OF_WORKING_YEARS'
    MARKS_PERCENT = 'NO_OF_WORKING_YEARS'
    EXCELLED_IN_ANY_SPOT = 'EXCELLED_IN_ANY_SPOT'
    EMPLOYED = 'EMPLOYED'
    DISABLED = 'DISABLED'

    name_choices = (
        (MIN_AGE, 'MIN_AGE'),
        (MAX_AGE, 'MAX_AGE'),
        (BANK_ACC_NO, 'BANK_ACC_NO'),
        (EDUCATIONAL_QUALIFICATION, 'EDUCATIONAL_QUALIFICATION'),
        (NATIONALITY, 'NATIONALITY'),
        (SAVINGS_ACC, 'SAVINGS_ACC'),
        (MAX_NO_OF_GIRL_CHILDREN, 'MAX_NO_OF_GIRL_CHILDREN'),
        (MAX_NO_OF_CHILDREN, 'MAX_NO_OF_CHILDREN'),
        (GENDER, 'GENDER'),
        (CASTE, 'CASTE'),
        (MARITAL_STATUS, 'MARITAL_STATUS'),
        (MIN_SALARY, 'MIN_SALARY'),
        (PREGNANT, 'PREGNANT'),
        (FARMER, 'FARMER'),
        (NO_OF_WORKING_YEARS, 'NO_OF_WORKING_YEARS'),
        (MARKS_PERCENT, 'NO_OF_WORKING_YEARS'),
        (EXCELLED_IN_ANY_SPOT, 'EXCELLED_IN_ANY_SPOT'),
        (EMPLOYED, 'EMPLOYED'),
        (DISABLED, 'DISABLED'),

    )

    # scheme = models.ForeignKey(Post)
    name = models.CharField(
        max_length=30,
        choices=name_choices)
    type_choices = (
        ('NUMERIC', 'NUMERIC'),
        ('LIST', 'LIST'),
        ('BOOLEAN', 'BOOLEAN'),
    )
    type = models.CharField(
        max_length=10,
        choices=type_choices,
    )
    Required_field = models.TextField()

    # Required_documents=models.ManyToManyField(Certificate_Proof)

    def __str__(self):
        return self.name + self.Required_field


class Post(models.Model):
    scheme_id = models.TextField(null=True)
    title = models.CharField(max_length=100)
    launch_date = models.DateField()
    is_active = models.BooleanField()
    slug = models.CharField(max_length=30)
    criteria = models.ManyToManyField(Scheme_criteria)
    required_documents = models.ManyToManyField(Documents)

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
        new_slug = "%s-%s" % (slug, qs.first().id)
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
