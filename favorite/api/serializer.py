from rest_framework import serializers
from visits.api.serializer import PatientSerializer
from favorite.models import Favorite


class FavoriteSerializerForDoctor(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
