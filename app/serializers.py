from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    PrimaryKeyRelatedField
    )

from .models import Post,Scheme_criteria,Documents

class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheme_criteria
        fields =('name',
                 'type',
                 'Required_field',
                 )

post_detail_url = HyperlinkedIdentityField(
    view_name='postss-api:DetailedView',
    lookup_field='slug',
)

class appCreateSerializer(ModelSerializer):
    class Meta:

        model = Post
        fields = ('title',
                  # 'crit',
                  'launch_date',
                  'url',
                  'is_active',
                  'slug',
                  )


class appDetailedSerializer(serializers.ModelSerializer):
    # html = SerializerMethodField()
    # criteria = PrimaryKeyRelatedField(many=True, read_only=True)
    # crit =SerializerMethodField()
    # url = post_detail_url

    class Meta:
        model = Post
        fields = ('title',
                  # 'criteria',
                  # 'crit',
                  'launch_date',
                  # 'url',
                  'is_active',
                  'slug',
                  )
    # def get_crit(self, obj):
    #     print(obj.criteria)
    #     print(object)
    #     print(1)
    #     c_qs = Scheme_criteria.objects.filter(obj.criteria)
    #     crit = CriteriaSerializer(c_qs, many=True).data
    #     return crit


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