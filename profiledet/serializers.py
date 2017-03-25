from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    SerializerMethodField
)
from .models import Profiledet


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiledet
        fields = '__all__'


class ProfileDetailedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profiledet
        fields='__all__'

    # def get_user(self, obj):
    #     return str(obj.user.username)
    #
    # def get_html(self, obj):
    #     return obj.get_markdown()


class ProfileSerializer(serializers.ModelSerializer):
#     url = HyperlinkedIdentityField(
#         view_name='postss-api:list',
#         lookup_field='title',
#     )

    class Meta:
        model = Profiledet
        fields = '__all__'
