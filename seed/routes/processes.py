"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Process
from app.serializers import ProcessSerializer

class ProcessViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = ProcessSerializer
    queryset = Process.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Process.filter_permissions(
            super().get_queryset(), Process.permission_filters(user))