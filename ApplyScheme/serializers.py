from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    SerializerMethodField
)
from .models import AppliedSchemes

class AppliedSchemesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedSchemes
        fields = (
            'scheme',
            'date_applied',
        )

class AppliedSchemesDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedSchemes
        fields = (
            'id',
            'user',
            'scheme',
            'date_applied',
        )
        # def get_user(self, obj):
        #     return str(obj.user.username)
        #
        # def get_html(self, obj):
        #     return obj.get_markdown()

class AppliedSchemesSerializer(serializers.ModelSerializer):
    #     url = HyperlinkedIdentityField(
    #         view_name='postss-api:list',
    #         lookup_field='title',
    #     )

    class Meta:
        model = AppliedSchemes
        fields = (
            'id',
            'user',
            'scheme',
            'date_applied',
        )
