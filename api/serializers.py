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
        fields = ["pk", "username", "password", "games"]
        extra_kwargs = {'password': {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get("username"),
            password=validated_data.get("password")
        )

        serializer = UserSerializer()

        return user


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
