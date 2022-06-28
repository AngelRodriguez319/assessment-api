"""
__Seed builder__
  Extended module
"""

import seed.routes.processes as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.serializers import ProcessSerializer
from domain.create_process import create_process


class ProcessViewSet(SeedRoute.ProcessViewSet):

    @action(detail=False, methods=['GET'])
    def execute(self, request):

        data = request.query_params
        has_fields_or_400(data, "N", "K", "user_id")

        try:
            n = int(data["N"])
            k = int(data["K"])
            user_id = int(data["user_id"])
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": "Value Error."})

        result = create_process(n, k, user_id)

        if result is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": "Value Error."})
        else:
            return Response(status=status.HTTP_201_CREATED, data=result)
