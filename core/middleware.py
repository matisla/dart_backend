from django.shortcuts import redirect
from django.urls import reverse


def login_middleware(get_response):
    def middleware(request, *args, **kwargs):

        if not request.user.is_authenticated and reverse("login") != request.path:
            return redirect("login")
        else:
            return get_response(request, *args, **kwargs)

    return middleware
