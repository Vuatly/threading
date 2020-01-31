from django.db import models


class Email(models.Model):
    text = models.CharField(max_length=150, verbose_name='Текст')
    email = models.EmailField(verbose_name='Почта')
    seconds = models.PositiveIntegerField(default=0, verbose_name='Секунды')

    def __str__(self):
        return self.email


