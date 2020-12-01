from django.apps import AppConfig


class RegistryMonitorConfig(AppConfig):
    name = 'apps.registry_monitor'
    def ready(self):
       # import apps.registry_monitor.signals
       pass
