from django.apps import AppConfig


class MegaSenaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MegaSena'

    def ready(self, *args, **kwargs) -> None:
        import MegaSena.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready

