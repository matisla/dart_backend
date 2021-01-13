from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    MAX_SCORE_CHOICES = ((301, 301), (501, 501), (701, 701))
    BEST_OF_CHOICES = (
        (3, 3),
        (5, 5),
        (7, 7),
        (9, 9),
    )
    MODE_CHOICES = (
        ("single", "single out"),
        ("master", "master out"),
        ("double", "double out"),
    )
    users = models.ManyToManyField(User)
    finished = models.BooleanField(default=False)
    best_of = models.IntegerField(default=3)
    max_score = models.IntegerField(choices=MAX_SCORE_CHOICES)
    mode = models.CharField(choices=MODE_CHOICES, max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        users = ", ".join([u.username for u in self.users.all()])
        return f"Game {self.id}"


class Set(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)


class Leg(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)


class Round(models.Model):
    leg = models.ForeignKey(Leg, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
