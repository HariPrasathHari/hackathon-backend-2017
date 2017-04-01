from django.apps import AppConfig


class ApplyschemeConfig(AppConfig):
    name = 'ApplyScheme'

    def ready(self):
        import ApplyScheme.signals