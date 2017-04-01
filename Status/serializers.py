from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    SerializerMethodField,
    ModelSerializer
)
from .models import StatusOfSchemes


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOfSchemes
        fields = (
            'id',
            'Status_of_scheme',
            'Scheme_id',
        )


class StatusEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOfSchemes
        fields = (
            'Status_of_scheme',
        )
