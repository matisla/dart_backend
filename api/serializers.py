from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import *


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = User
        fields = ["pk", "username", "games"]


class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set
        fields = "__all__"


class LegSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leg
        fields = "__all__"


class RoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leg
        fields = "__all__"


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
