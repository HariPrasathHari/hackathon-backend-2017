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
from .models import AppliedSchemes
from .serializers import (
    AppliedSchemesSerializer,
    AppliedSchemesDetailedSerializer,
    AppliedSchemesCreateSerializer,
    )

from app.permissions import IsOwnerorObjectReadOnly
from app.paginations import PostPageNumberPagination,PostLimitOffset


# Create your views here.


class SchemeList(ListAPIView):
    serializer_class = AppliedSchemesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    pagination_class = PostPageNumberPagination
    search_fields = ['title', 'date', 'slug', 'min_age', 'max_salary']
    def get_queryset(self,*args,**kwargs):
        queryset_list = AppliedSchemes.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(date__icontains=query)
            ).distinct()
        return queryset_list

class AppliedSchemeCreate(CreateAPIView):
    queryset = AppliedSchemes.objects.all()
    serializer_class = AppliedSchemesCreateSerializer
    permission_classes = [IsOwnerorObjectReadOnly,IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class SchemeDetailedList(RetrieveAPIView):
    queryset = AppliedSchemes.objects.all()
    serializer_class = AppliedSchemesDetailedSerializer
    # lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthenticated]

class SchemeUpdateList(RetrieveUpdateAPIView):
    queryset = AppliedSchemes.objects.all()
    serializer_class = AppliedSchemesSerializer
    # lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsOwnerorObjectReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class SchemeDeleteList(DestroyAPIView):
    queryset = AppliedSchemes.objects.all()
    serializer_class = AppliedSchemesSerializer
    # lookup_field = 'slug'
    permission_classes = [IsOwnerorObjectReadOnly, IsAuthenticated]