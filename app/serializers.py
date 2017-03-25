from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )

from .models import Post


# Create your tests here.

post_detail_url = HyperlinkedIdentityField(
    view_name='postss-api:Detailedview',
    lookup_field='title',
)
class appCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('body',
                  'date')


class appDetailedSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    html = SerializerMethodField()

    url = post_detail_url
    class Meta:
        model = Post
        fields = ('url', 'id', 'user', 'html', 'title', 'date', 'body')

    def get_user(self, obj):
        return str(obj.user.username)

    def get_html(self, obj):
        return obj.get_markdown()


class appSerializer(serializers.HyperlinkedModelSerializer):

    url = post_detail_url
    class Meta:
        model = Post
        fields = ('id', 'date', 'title', 'url')
