from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *

import logging

logger = logging.getLogger(__name__)

class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer

    def list(self, request, **kwargs):
        game_id = request.GET.get("game_id")
        game = get_object_or_404(Game, pk=game_id)

        serializer = ScoreSerializer(game)

        return Response(serializer.data)

    def create(self, request, **kwargs):
        return Response()

