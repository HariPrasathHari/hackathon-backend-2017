"""
'''
from profiledet.serializers import ProfileDetailedSerializer
from app.models import Post
from app.serializers import appSerializer
from profiledet.models import ProfileDet
from profiledet.models import Profiledet
obj=Profiledet.objects.first()
obj_data = ProfileDetailedSerializer(obj)
print(obj_data.data)

'''
"""
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

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
        profile_instance = User.objects.get(user=request.user)
        usernames = [user.id for user in User.objects.all()]
        return Response(usernames)
