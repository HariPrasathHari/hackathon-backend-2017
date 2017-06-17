"""
'''
from profiledet.serializers import ProfileDetailedSerializer
from app.models import Post
from app.serializers import appSerializer
from datacenter.models import *
from profiledet.models import Profiledet
obj=User.objects.first()
obj_data = ProfileDetailedSerializer(obj)
print(obj_data.data)

'''
"""
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from app.serializers import *

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from .models import *
from datacenter.models import *
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,

    RetrieveUpdateAPIView,
    GenericAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from profiledet.models import Profiledet
from .serializers import (
    appSerializer,
    appDetailedSerializer,
    appCreateSerializer,
)
from profiledet.permissions import IsGovernmentOfficial

from .permissions import IsOwnerorObjectReadOnly
from .paginations import PostPageNumberPagination, PostLimitOffset


# Create your views here.
def hello(request):
    return render(request, 'app/home.html')


def contact(request):
    return render(request, 'app/cms.html', {'content': ['hi ', 'this is hari', 'my number is 94886028282']})


def home(request):
    return render(request, 'app/home.html', {'content': ['active', '', '']})


def register(request):
    return render(request, 'app/register.html')


def invalid(request):
    return render(request, 'app/home.html')


class SchemeList(ListAPIView):
    serializer_class = appDetailedSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    # pagination_class = PostPageNumberPagination
    search_fields = ['title', 'date', 'slug', 'min_age', 'max_salary']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(date__icontains=query)
            ).distinct()
        return queryset_list


class SchemeCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = appCreateSerializer
    permission_classes = [IsAuthenticated, IsGovernmentOfficial]

    def perform_create(self, serializer):
        serializer.save()


class SchemeDetailedList(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = appDetailedSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


class SchemeUpdateList(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = appCreateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsGovernmentOfficial]

    def perform_create(self, serializer):
        serializer.save()


class SchemeDeleteList(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = appDetailedSerializer
    lookup_field = 'slug'
    permission_classes = [IsGovernmentOfficial]


class GetEligibleSchemes(APIView):
    def get(self, request, format=None):
        profile_instance = request.user
        # aadhar_no = profile_instance.username
        aadhar_no = '123456789012'
        aadhar_id = aadhar_Database.objects.get(bank=aadhar_no)
        if BGateway_database.objects.filter(Aadhar_no=aadhar_id).exists():
            has_bank_ac = True
        else:
            has_bank_ac = False
        # other_data = aadhar_Database.objects.get(bank=aadhar_no)
        dob_year = aadhar_id.dob.year
        age = timezone.now().year - dob_year
        print(has_bank_ac, age)
        # list_scheme = Post.objects.filter(scheme_criteria_id__BANK_ACC_NO=has_bank_ac).filter(scheme_criteria_id__MIN_AGE__gte=age).filter(scheme_criteria_id__MAX_AGE__lte=age)
        list_scheme = Post.objects.filter(scheme_criteria_id_verticals__MIN_AGE__gte=age)
        final_list = []
        for scheme in list_scheme:
            serial_data = appDetailedSerializer(scheme).data
            final_list.append(serial_data)
        print(final_list)

        # usernames = [user.id for user in User.objects.all()]
        # print(list_scheme)
        # serial_data = appDetailedSerializer(list_scheme)
        # # print(serial_data)
        # print(serial_data.data)
        return Response(final_list)


class GetEligibleSchemesFinal(APIView):
    def get(self, request):
        aadhar_no = '123456789012'
        aadhar_id = aadhar_Database.objects.get(bank=aadhar_no)
        final_list = []
        return Response(final_list)