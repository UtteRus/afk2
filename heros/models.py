from django.db import models

class Hero(models.Model):
    hero_name = models.CharField(max_length=255, null=True)
    fraction = models.CharField(max_length=255, null=True)
    img_hero = models.ImageField(upload_to="hero", null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
