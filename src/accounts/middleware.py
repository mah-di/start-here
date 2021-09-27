from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from .custom_configs import (
    LOGIN_REQUIRED_EXEMPT_URLS,
    UNAUTHENTICATED_SPECIFIC_URLS,
    LOGIN_REDIRECT_URL,
    LOGIN_URL,
    )


class UnauthenticatedSpecificMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'), "Unauthenticated Specific Middleware"
        if request.user.is_authenticated:
            path = request.path.lstrip('/')
            if any(path.startswith(url) for url in UNAUTHENTICATED_SPECIFIC_URLS):
                return redirect(LOGIN_REDIRECT_URL)
        
        return None


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'), "Login Required Middleware"
        if not request.user.is_authenticated:
            path = request.path.lstrip('/')
            if not any(path.startswith(url) for url in LOGIN_REQUIRED_EXEMPT_URLS):
                login_redirect = f"{LOGIN_URL}?next={request.path_info}"
                return redirect(login_redirect)
        
        return None