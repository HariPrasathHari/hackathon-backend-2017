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
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from .models import Post
from .serializers import (
    appSerializer,
    appDetailedSerializer,
    appCreateSerializer,
    )

from .permissions import IsOwnerorObjectReadOnly
from .paginations import PostPageNumberPagination,PostLimitOffset


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
    serializer_class = appSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    pagination_class = PostPageNumberPagination
    search_fields = ['title', 'date', 'slug', 'min_age', 'max_salary']
    def get_queryset(self,*args,**kwargs):
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
    # permission_classes = [IsAuthenticated,IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

class SchemeDetailedList(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = appDetailedSerializer
    lookup_field = 'slug'
    # permission_classes = [IsAuthenticatedOrReadOnly]

class SchemeUpdateList(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = appCreateSerializer
    lookup_field = 'slug'
    # permission_classes = [IsAuthenticated, IsOwnerorObjectReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class SchemeDeleteList(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = appDetailedSerializer
    lookup_field = 'slug'
    # permission_classes = [IsOwnerorObjectReadOnly]