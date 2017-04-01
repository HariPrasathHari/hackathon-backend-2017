from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    )

from .models import Post



post_detail_url = HyperlinkedIdentityField(
    view_name='postss-api:DetailedView',
    lookup_field='slug',
)

class appCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title',
                  'criteria',
                  'launch_date',
                  'url',
                  'is_active',
                  'slug',
                  )


class appDetailedSerializer(serializers.ModelSerializer):
    # html = SerializerMethodField()

    url = post_detail_url
    class Meta:
        model = Post
        fields = ('title',
                  'criteria',
                  'launch_date',
                  'url',
                  'is_active',
                  'slug',
                  )



class appSerializer(serializers.ModelSerializer):
    url = post_detail_url
    class Meta:
        model = Post
        fields = ('title',
                  'criteria',
                  'launch_date',
                  'url',
                  'is_active',
                  'slug',
                  )