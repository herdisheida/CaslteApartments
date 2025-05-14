from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # URLs that don't require login
        self.allowed_urls = [
            reverse("login"),
            reverse("register"),
            "/admin/",
            "/static/",
            "/media/",
            "/favicon.ico",
        ]

    def __call__(self, request):
        # skip check for allowed URLs
        if any(request.path.startswith(url) for url in self.allowed_urls):
            return self.get_response(request)

        # go to log-in if not authenticated
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")

        return self.get_response(request)
