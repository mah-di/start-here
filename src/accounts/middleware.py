from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'), "Custom Login Required Middleware"
        if not request.user.is_authenticated:
            path = request.path.lstrip('/')
            if not any(path.startswith(url) for url in settings.LOGIN_REQUIRED_EXEMPT_URLS):
                login_redirect = f"{settings.LOGIN_URL}?next={request.path_info}"
                return redirect(login_redirect)
        
        return None