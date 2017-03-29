from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.conf import settings
from ApplyScheme.models import AppliedSchemes

class StatusOfSchemes(models.Model):
    Scheme_id = models.OneToOneField(AppliedSchemes, auto_created=True)
    APPLIED = 'AP'
    CHECKING = 'CH'
    TRANSACTION = 'TR'
    COMPLETED = 'CO'
    Status_of = (
        (APPLIED, 'applied'),
        (CHECKING, 'verification'),
        (TRANSACTION, 'transaction on process'),
        (COMPLETED, 'finished transaction'),
    )
    Status_of_scheme = models.CharField(
        max_length=2,
        choices=Status_of,
        default=APPLIED,
    )
    def is_upperclass(self):
        return self.Status_of_scheme in (self.COMPLETED, self.TRANSACTION, self.APPLIED, self.CHECKING)


    def __str__(self):
        return self.Status_of_scheme.Status_Of
