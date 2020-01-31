from django.apps import AppConfig


class MailServiceConfig(AppConfig):
    name = 'emailsender'

    def ready(self):
        import emailsender.signals
