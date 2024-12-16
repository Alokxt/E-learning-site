from django.apps import AppConfig


class BunchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bunch'

    def ready(self):
        import bunch.signals
        ___all__ = bunch.signals

    

    

   
