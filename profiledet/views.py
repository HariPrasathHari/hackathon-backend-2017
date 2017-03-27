from django.shortcuts import render
from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
    GenericAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .models import Profiledet
from .serializers import (
    ProfileDetailedSerializer,
    ProfileSerializer,
    ProfileCreateSerializer,
)

from profiledet.permissions import IsOwnerorObjectReadOnly
from app.paginations import PostPageNumberPagination, PostLimitOffset


class ProfileList(ListAPIView):
    serializer_class = ProfileSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    pagination_class = PostPageNumberPagination
    search_fields = ['age', 'community', 'first_name', 'last_name', 'middle_name']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Profiledet.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(age__icontains=query) |
                Q(middle_name__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            ).distinct()
        return queryset_list


class ProfileDetailedList(RetrieveAPIView):
    queryset = Profiledet.objects.all()
    serializer_class = ProfileDetailedSerializer
    lookup_field = 'user'
    permission_classes = [AllowAny]


class ProfileCreate(RetrieveUpdateAPIView):
    queryset = Profiledet.objects.all()
    serializer_class = ProfileCreateSerializer
    permission_classes = [IsOwnerorObjectReadOnly, IsAuthenticated]
    lookup_field = 'user'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     return self.create()


class ProfileUpdateList(RetrieveUpdateAPIView):
    queryset = Profiledet.objects.all()
    serializer_class = ProfileCreateSerializer
    lookup_field = 'user'
    permission_classes = [IsAuthenticated, IsOwnerorObjectReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
