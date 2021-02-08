from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from api.serializers import *
from core.models import *

import logging

logger = logging.getLogger(__name__)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def list(self, request):
        filters = {}

        if "username" in request.GET:
            filters["users__username"] = request.GET["username"]

        if "finished" in request.GET:
            filters["finished"] = request.GET["finished"].lower() == "true"

        if filters:
            queryset = Game.objects.filter(**filters)
        else:
            queryset = Game.objects.all()

        context = {
            "request": request,
        }

        serializer = GameSerializer(queryset, many=True, context=context)

        return Response(serializer.data)


@api_view(["GET"])
def user_detail(request, username):
    print(f"requested {username}")
    user = User.objects.get_object_or_404(username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)
