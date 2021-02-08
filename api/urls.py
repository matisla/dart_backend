from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

from api import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("games", views.GameViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth-token", authtoken_views.obtain_auth_token, name="api-auth-token"),
    path("api-auth/", include("rest_framework.urls")),
]
