import threading
import time

from django.core.mail import send_mail
from django.db.models.signals import post_save
from .models import Email


def sending_email(sender, instance, **kwargs):
    time.sleep(instance.seconds)
    send_mail('Рассылочка из Джанги',
              instance.text,
              'От кого',
              [instance.email],
              fail_silently=False
              )
    Email.objects.filter(id=instance.id).update(seconds=0)


def manage_func(sender, instance, **kwargs):
    thread = threading.Thread(target=sending_email, args=(sender, instance), kwargs=kwargs)
    thread.start()


post_save.connect(manage_func, sender=Email)

