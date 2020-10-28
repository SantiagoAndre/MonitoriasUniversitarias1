from django.apps import AppConfig


class MonitorConfig(AppConfig):
    name = 'apps.monitor'
    def ready(self):
        import apps.monitor.signals
