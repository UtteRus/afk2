from django.contrib.auth.models import User
from rest_framework import serializers
from heros.models import Specifications, Hero
from .models import Profile


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id_account']

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)


class RegistrationSerializers(serializers.ModelSerializer):
    profile = ProfileSerializers()

    class Meta:
        model = User
        fields = ['username', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user_id=user.pk,
                               **profile_data)
        for heros in Hero.objects.all():
            Specifications.objects.create(user_id=user.pk, hero_id=heros.pk)
        return user
