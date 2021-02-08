from django.contrib.auth.models import User

from rest_framework import serializers

from .models import *

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

class ScoreSerializer(serializers.Serializer):

    def create(self, **kwargs):
        return Round.objects.create(**self.validated_data)

