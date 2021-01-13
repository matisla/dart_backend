from django.urls import include, path

from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("games", views.GameViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth", include("rest_framework.urls")),
]
