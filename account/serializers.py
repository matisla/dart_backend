from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import Game

class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.none())

    class Meta:
        model = User
        fields = ["email", "username", "password", "games"]
        extra_kwargs = {'password': {"write_only": True}}

    def create(self):
        user = User.objects.create_user(
            email=self.validated_data.get("email"),
            username=self.validated_data.get("username"),
            password=self.validated_data.get("password")
        )

        return user

    def delete(self, username):
        user = User.objects.get(username=username)

        if user:
            user.delete()

        return user

