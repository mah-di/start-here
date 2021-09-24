from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, UserCreationForm, PasswordChangeForm
from django.utils.translation import ugettext as _


class RegistrationForm(UserCreationForm):
    is_active = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_active']
        extra_kwargs = {'is_active': {'value': False}}


class CustomSetPasswordForm(SetPasswordForm):
    error_messages = {
        **SetPasswordForm.error_messages,
        'same_password' : _("New password cannot be the same as current password."),
    }
    
    def clean_new_password2(self):
        response = super().clean_new_password2()
        if self.user.check_password(self.cleaned_data['new_password1']):
            raise forms.ValidationError(self.error_messages['same_password'], code='same_password')

        return response


class CustomPasswordChangeForm(PasswordChangeForm):
    error_messages = {
        **PasswordChangeForm.error_messages,
        'same_password' : _("New password cannot be the same as the old password."),
    }
    
    def clean_new_password2(self):
        response = super().clean_new_password2()
        if self.cleaned_data.get('new_password1') == self.cleaned_data.get('old_password'):
            raise forms.ValidationError(self.error_messages['same_password'], code='same_password')

        return response


class CustomPasswordResetForm(PasswordResetForm):
    error_messages = {
        'nonexistant_email' : _("There is no account in our system associated with this email."),
        'unverified_email' : _('Please verify your email first.'),
    }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError(self.error_messages['nonexistant_email'], code='nonexistant_email')

        if not user.is_active:
            raise forms.ValidationError(self.error_messages['unverified_email'], code='unverified_email')

        return email


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        **AuthenticationForm.error_messages,
        'unverified' : _("Please verify your email before trying to login."),
    }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username, is_active=False).exists():
            raise forms.ValidationError(self.error_messages['unverified'], code='unverified')

        return username