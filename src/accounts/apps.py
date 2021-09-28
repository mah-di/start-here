from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        response = super().ready()
        from django.conf import settings
        from . import configs
        for attr in dir(configs):

            if not hasattr(settings, attr):
                setattr(settings, attr, getattr(configs, attr))
            elif type(getattr(configs, attr)) == list and hasattr(settings, attr):
                settings_attr = getattr(settings, attr)
                settings_attr += getattr(configs, attr)
                setattr(settings, attr, settings_attr)

        MIDDLEWARES = getattr(settings, 'MIDDLEWARE')
        MIDDLEWARES += [
            'accounts.middleware.UnauthenticatedSpecificMiddleware',
            'accounts.middleware.LoginRequiredMiddleware',
        ]
        setattr(settings, 'MIDDLEWARE', MIDDLEWARES)

        return response