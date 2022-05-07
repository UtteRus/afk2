from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    id_account = models.IntegerField(verbose_name='ид аккаунта')
    position_in_the_guild = models.CharField(verbose_name='должность в '
                                                          'гильдии',
                                             max_length=255)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user.username}'
