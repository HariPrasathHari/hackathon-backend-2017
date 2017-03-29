from django.shortcuts import render
from django.db.models import Q
from .models import AppliedSchemes, StatusOfSchemes
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from profiledet.permissions import IsGovernmentOfficial
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

from .serializers import StatusSerializer
from app.permissions import IsOwnerorObjectReadOnly
from app.paginations import PostPageNumberPagination, PostLimitOffset


class StatusList(ListAPIView):
    serializer_class = StatusSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated,
                          IsGovernmentOfficial]
    pagination_class = PostPageNumberPagination
    search_fields = [
        'Status_of_scheme',
        'Scheme_id',
    ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = StatusOfSchemes.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(Status_of_scheme__icontains=query) |
                Q(Scheme_id__icontains=query)
            ).distinct()
        return queryset_list
