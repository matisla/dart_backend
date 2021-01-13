from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import *
from .forms import *


def index(request):
    context = {"games": Game.objects.filter(users=request.user, finished=False)}

    return render(request, "core/index.html", context)


def game_update(request, pk):

    game = Game.objects.get(pk=pk)
    context = {"game": game}

    return render(request, "core/game_update.html", context)


def game_detail(request, pk):

    user_id = request.GET.get("player", None)
    if user_id is None:
        return game_update(request, pk)

    player = User.objects.get(username=user_id)
    game = Game.objects.get(pk=pk)

    form = ScoreForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        pass
        # Round.objects.create()

    context = {"game": game, "selected_player": player, "form": form}

    return render(request, "core/game_detail.html", context)


def login_create_view(request):
    context = {}

    return (request, "registration/login.html", context)


class UserDetailView(DetailView):
    model = User


class GameDetailView(DetailView):
    model = Game


class RoundCreateView(CreateView):
    model = Round
    fields = "__all__"
    template_name = "core/forms.html"


class GameCreateView(CreateView):
    model = Game
    fields = "__all__"
    template_name = "core/forms.html"
    success_url = reverse_lazy("round-create")
