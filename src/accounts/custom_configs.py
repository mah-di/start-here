from django.conf import settings


LOGIN_REQUIRED_EXEMPT_URLS = settings.LOGIN_REQUIRED_EXEMPT_URLS if hasattr(settings, 'LOGIN_REQUIRED_EXEMPT_URLS') else []
LOGIN_REQUIRED_EXEMPT_URLS += [
    'accounts/register/',
    'accounts/login/',
    'accounts/verify/',
    'accounts/resend-verification/',
    'accounts/password-reset/',
    'accounts/password-reset/done/',
    'accounts/password-reset/confirm/',
    'accounts/password-reset/complete/',
]


UNAUTHENTICATED_SPECIFIC_URLS = settings.UNAUTHENTICATED_SPECIFIC_URLS if hasattr(settings, 'UNAUTHENTICATED_SPECIFIC_URLS') else []
UNAUTHENTICATED_SPECIFIC_URLS += [
    'accounts/register/',
    'accounts/login/',
    'accounts/verify/',
    'accounts/resend-verification/',
]


LOGIN_URL = settings.LOGIN_URL


LOGIN_REDIRECT_URL = settings.LOGIN_REDIRECT_URL