from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import *

import logging

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer

    def list(self, request, **kwargs):
        if request.GET:
            queryset = User.objects.filter(**request.GET)
        else:
            queryset = User.objects.all()

        context = {
            "request": request,
        }

        serializer = UserSerializer(queryset, many=True, context=context)

        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        user = get_object_or_404(User, username=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = UserSerializer(data=request.data)
        data = None

        if serializer.is_valid():
            serializer.create()
            data = serializer.data

        else:
            data = serializer.errors

        return Response(data)

    def delete(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()

        return Response(serializer)