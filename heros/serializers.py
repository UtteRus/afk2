from rest_framework import serializers
from .models import Specifications, Hero


class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specifications
        fields = ['pk', 'named_item', 'furniture', 'engraving',
                  'evolution', 'hair', ]


class SpecificationsHireSerializer(serializers.ModelSerializer):
    available_heroes = serializers.IntegerField(choices=[
        (value.pk, value.hero_name) for value in Hero.objects.all()])


