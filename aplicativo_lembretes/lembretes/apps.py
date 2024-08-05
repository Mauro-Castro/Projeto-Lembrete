from django.apps import AppConfig

class LembretesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lembretes'

    def ready(self):
        import lembretes.signals
