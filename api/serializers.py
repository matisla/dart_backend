from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


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
