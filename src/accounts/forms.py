from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm, PasswordChangeForm
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
