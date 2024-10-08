from django.apps import AppConfig


class SingnalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'singnalapp'
    def ready(self):
        import singnalapp.signals


    