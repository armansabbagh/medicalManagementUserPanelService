from rest_framework import serializers
from visits.models import VisitTime
from users.models import NormalUser


class VisitSerializerForDoctor(serializers.ModelSerializer):
    duration = serializers.IntegerField(allow_null=True)
    endTime = serializers.TimeField(allow_null=True)

    class Meta:
        model = VisitTime
        fields = ('date', 'time', 'duration', 'endTime')


class VisitSerializerForUser(serializers.ModelSerializer):
    time_id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = VisitTime
        fields = 'time_id'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        fields = '__all__'


class VisitListSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = VisitTime
        fields = "__all__"
