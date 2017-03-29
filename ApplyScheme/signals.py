from django.db.models.signals import pre_save,post_save
from Status.models import StatusOfSchemes
from .models import AppliedSchemes

def create_user(instance, new_user=None):
    if new_user is None:
        new_user = instance.request.user
        user = new_user
    return user

def pre_save_AppliedSchemes_receiver(sender, instance, *args, **kwargs):
    if not instance.user:
        instance.user = create_user(instance)

def post_save_AppliedSchemes_receiver(sender, instance, *args, **kwargs):
    StatusOfSchemes.objects.create(Scheme_id=instance)


pre_save.connect(pre_save_AppliedSchemes_receiver, sender=AppliedSchemes)

post_save.connect(post_save_AppliedSchemes_receiver, sender=AppliedSchemes)
