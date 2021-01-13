from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("<int:pk>", UserDetailView.as_view(), name="user-details"),
    path("new_game", GameCreateView.as_view(), name="game-create"),
    path("game/<int:pk>", game_detail, name="game"),
    path("<int:pk>/new_round", RoundCreateView.as_view(), name="round-create"),
]
