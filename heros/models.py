from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class HelpChoice:
    ELITE = 'Elite'
    ELITE_PLUS = 'Elite+'
    LEGENDARY = 'Legendary'
    LEGENDARY_PLUS = 'Legendary+'
    MYTHICAL = 'Mythical'
    MYTHICAL_PLUS = 'Mythical+'
    EXALTED = 'Exalted'
    EXALTED1 = 'Exalted1 '
    EXALTED2 = 'Exalted2'
    EXALTED3 = 'Exalted3'
    EXALTED4 = 'Exalted4'
    EXALTED5 = 'Exalted5'
    EVOLUTION = [
        (ELITE, 'Элитный'),
        (ELITE_PLUS, 'Элитный+'),
        (LEGENDARY, 'Легендарный'),
        (LEGENDARY_PLUS, 'Легендарный+'),
        (MYTHICAL, 'Мифический'),
        (MYTHICAL_PLUS, 'Мифический+'),
        (EXALTED, 'Возвышенный'),
        (EXALTED1, 'Возвышенный 1'),
        (EXALTED2, 'Возвышенный 2'),
        (EXALTED3, 'Возвышенный 3'),
        (EXALTED4, 'Возвышенный 4'),
        (EXALTED5, 'Возвышенный 5'),
    ]
    RATING_HERO = [
        ('S+', 'S+'),
        ('S', 'S'),
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('D+', 'D+'),
        ('D', 'D')
    ]


class Hero(models.Model):
    hero_name = models.CharField(max_length=255, null=True,
                                 verbose_name='Имя героя')
    fraction = models.CharField(max_length=255, null=True,
                                verbose_name='Фракция')
    img_hero = models.ImageField(upload_to="hero", null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    named_item_recommended = models.IntegerField(default=0,
                                                 verbose_name='необходимый'
                                                              ' именной '
                                                              'предмет',
                                                 validators=[
                                                     MinValueValidator(0),
                                                     MaxValueValidator(40)
                                                 ])
    furniture_recommended = models.IntegerField(default=0,
                                                verbose_name='необходимая '
                                                             'мебель',
                                                validators=[
                                                    MinValueValidator(0),
                                                    MaxValueValidator(9)
                                                ])

    engraving_recommended = models.IntegerField(default=0,
                                                verbose_name='необходимая '
                                                             'гравировка',
                                                validators=[
                                                    MinValueValidator(0),
                                                    MaxValueValidator(90)
                                                ])

    evolution = models.CharField(choices=HelpChoice.EVOLUTION,
                                 default=HelpChoice.ELITE,
                                 verbose_name='развитие персонажа',
                                 max_length=20)
    pve_rating = models.CharField(choices=HelpChoice.RATING_HERO,
                                  default=HelpChoice.RATING_HERO[0],
                                  verbose_name='рейтинг пве',
                                  max_length=2)
    pvp_rating = models.CharField(choices=HelpChoice.RATING_HERO,
                                  default=HelpChoice.RATING_HERO[0],
                                  verbose_name='рейтинг пвп',
                                  max_length=2)
    distorted_world_rating = models.CharField(choices=HelpChoice.RATING_HERO,
                                              default=HelpChoice.RATING_HERO[
                                                  0],
                                              verbose_name='рейтинг '
                                                           'искаженный мир',
                                              max_length=2)
    events_rating = models.CharField(choices=HelpChoice.RATING_HERO,
                                     default=HelpChoice.RATING_HERO[0],
                                     verbose_name='рейтинг ивент',
                                     max_length=2)
    damn_world_rating = models.CharField(choices=HelpChoice.RATING_HERO,
                                         default=HelpChoice.RATING_HERO[0],
                                         verbose_name='рейтинг проклятый мир',
                                         max_length=2)
    abyss_rating = models.CharField(choices=HelpChoice.RATING_HERO,
                                    default=HelpChoice.RATING_HERO[0],
                                    verbose_name='рейтинг бездны',
                                    max_length=2)

    class Meta:
        verbose_name = 'Герои'
        verbose_name_plural = 'Герои'
        ordering = ['hero_name']

    def __str__(self):
        return self.hero_name


class Specifications(models.Model):
    named_item = models.IntegerField(default=0,
                                     verbose_name='именной предмет',
                                     validators=[
                                         MinValueValidator(0),
                                         MaxValueValidator(40)
                                     ])
    furniture = models.IntegerField(default=0, verbose_name='мебель',
                                    validators=[
                                        MinValueValidator(0),
                                        MaxValueValidator(9)
                                    ])
    engraving = models.IntegerField(default=0, verbose_name='гравировка',
                                    validators=[
                                        MinValueValidator(0),
                                        MaxValueValidator(90)
                                    ])
    evolution = models.CharField(choices=HelpChoice.EVOLUTION,
                                 default=HelpChoice.ELITE, blank=False,
                                 verbose_name='Развитие персонажа',
                                 max_length=20)
    hair = models.BooleanField(verbose_name='найм', default=False)
    date_update_specifications = models.DateTimeField(auto_now=True,
                                                      verbose_name='дата '
                                                                   'изменения')
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE,
                             verbose_name='герой')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Спецификации героев'
        verbose_name_plural = 'Спецификации героев'
        ordering = ['hero']

    def __int__(self):
        return self.pk
