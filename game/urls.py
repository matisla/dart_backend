from django.urls import include, path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register("Games", GameViewSet)
router.register("Scores", ScoreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
