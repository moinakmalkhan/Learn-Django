from django.apps import AppConfig


class SignalappConfig(AppConfig):
    name = 'signalapp'
    def ready(self):
        import signalapp.signals
