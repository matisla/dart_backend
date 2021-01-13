from django import template
from django.db.models import Sum

from ..models import *


register = template.Library()


@register.simple_tag
def nb_sets(game, user):
    return Set.objects.filter(game=game, winner=user).count()


@register.simple_tag
def nb_legs(game, user):
    return Leg.objects.filter(set__game=game, winner=user).count()


@register.simple_tag
def score(game, user):
    rounds = Round.objects.filter(
        leg__set__game=game, leg__winner=None, user=user
    ).aggregate(total=Sum("score"))

    return game.max_score - (rounds["total"] or 0)
