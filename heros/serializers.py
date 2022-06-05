from rest_framework import serializers
from .models import Specifications, Hero


class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specifications
        fields = ['pk', 'named_item', 'furniture', 'engraving',
                  'evolution', 'hair', ]


class SpecificationsHireSerializer(serializers.ModelSerializer):
    # choi = [
    #     (value.pk, value.hero_name) for value in Hero.objects.all()]
    choi = Hero.objects.all().values_list('pk', 'hero_name')
    available_heroes = serializers.ChoiceField(choices=choi)

    class Meta:
        model = Specifications
        fields = ['available_heroes', 'named_item']


