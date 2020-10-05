from django.apps import AppConfig


class LearningGraphConfig(AppConfig):
    name = 'apps.learning_graph'
    def ready(self):
        import apps.learning_graph.signals