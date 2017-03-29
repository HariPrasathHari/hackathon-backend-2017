from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    SerializerMethodField
)
from .models import StatusOfSchemes


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOfSchemes
        fields = (
            'Status_of_scheme',
            'Scheme_id',
        )
