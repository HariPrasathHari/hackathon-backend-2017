from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
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
                  'date',
                  'min_age',
                  'max_salary',
                  'req_community',
                  )


class appDetailedSerializer(serializers.ModelSerializer):
    # html = SerializerMethodField()

    url = post_detail_url
    class Meta:
        model = Post
        fields = ('title',
                  'slug',
                  'date',
                  'min_age',
                  'max_salary',
                  'req_community',
                  'url',
                  )



class appSerializer(serializers.ModelSerializer):
    url = post_detail_url
    class Meta:
        model = Post
        fields = ('title',
                  'date',
                  'min_age',
                  'max_salary',
                  'url',
                  'req_community',
                  'slug',
                  )

