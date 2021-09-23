from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    LoginView,
    LogoutView
    )
from .forms import CustomPasswordChangeForm, CustomSetPasswordForm




urlpatterns = [
    path('', views.account, name='account'),
    path('register/', views.register, name='register'),
    path('verify/<uemb64>/<token>/', views.verify_account, name='email_verify'),
    path('resend-verification/', views.resend_verification, name='resend_verification'),
    path(
        'login/',
        LoginView.as_view(
            template_name = 'accounts/login.html',
            # redirect_field_name = name of a GET field (default = 'next'),
            # authentication_form = an instance of django.contrib.auth.forms.AuthenticationForm,
            # extra_context = {context: 'data'},
            # redirect_authenticated_user = bool -> determines whether to redirect already authenticated users as per successful login or not (default = False)
            # success_url_allowed_hosts = set of safe for redirecting hosts after login (default = [])
            ),
        name='login'),
    path(
        'logout/',
        LogoutView.as_view(
            template_name = 'accounts/logout.html',
            next_page = reverse_lazy('login'),
            # redirect_field_name = name of a GET field (default = 'next'),
            # extra_context = {context: 'data'},
            # success_url_allowed_hosts = set of safe for redirecting hosts after logout (default = [])
        ),
        name = 'logout'),
    path(
        'password-reset/',
        PasswordResetView.as_view(
            template_name = 'accounts/password_reset.html',
            success_url = reverse_lazy('password_reset_done'),
            # form_class = an instance of django.contrib.auth.forms.PasswordResetForm,
            # email_template_name = name of template used for generating password reset email (default = registration/password_reset_email.html)
            # subject_template_name = name of template used to generate the email subject (default = registration/password_reset_subject.txt),
            # token_generator = token for password resetting request (default = default_token_generator),
            # from_email = self explanatory,
            # extra_context = {context: 'data'},
            # html_email_template_name = name of template used to generate html/text multipart email,
            # extra_email_context = {context: 'data that will be available in the email template'},
        ),
        name='password_reset'),
    path(
        'password-reset/done/',
        PasswordResetDoneView.as_view(
            template_name = 'accounts/password_reset_done.html',
            # extra_context = {context: 'data'},
        ),
        name='password_reset_done'),
    path(
        'password-reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name = 'accounts/password_reset_confirm.html',
            success_url = reverse_lazy('password_reset_complete'),
            form_class = CustomSetPasswordForm,
            # token_generator = instance of the class to check the password (default = default_token_generator),
            # post_reset_login = bool -> determine whether to authenticate user after successful password reset (default = False),
            # post_reset_login_backend = path to the authentication backend for authenticating a user if post_reset_login is True (default = None),
            # extra_context = {context: 'data'},
            # reset_url_token = token parameter displayed as a component of password reset URLs (default = 'set-password'),
        ),
        name='password_reset_confirm'),
    path(
        'password-reset/complete/',
        PasswordResetCompleteView.as_view(
            template_name = 'accounts/password_reset_complete.html',
            # extra_context = {context: 'data'},
        ),
        name='password_reset_complete'),
    path(
        'password-change/',
        PasswordChangeView.as_view(
            template_name = 'accounts/password_change.html',
            success_url = reverse_lazy('password_change_done'),
            form_class = CustomPasswordChangeForm, 
            # extra_context = {context: 'data'},
        ),
        name='password_change'),
    path(
        'password-change/done/',
        PasswordChangeDoneView.as_view(
            template_name = 'accounts/password_change_done.html',
            # extra_context = {context: 'data'},
        ),
        name='password_change_done'),
]