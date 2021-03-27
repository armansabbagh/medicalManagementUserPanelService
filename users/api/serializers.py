from rest_framework import serializers
from users.models import *


class AdminCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            user_type=0,
            is_superuser=True,
            is_staff=True,
            **validated_data
        )

        return user


class NormalUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        fields = [
            'birth_date',
            'national_code',
            'phone',
            'home_phone',
            'address',
            'disease',
            'disease_detail'
        ]


class NormalUserCreateSerializer(serializers.ModelSerializer):
    normal_user_info = NormalUserDetailSerializer()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'normal_user_info'
        ]

    def create(self, validated_data):
        normal_user_data = validated_data.pop('normal_user_info')
        user = User.objects.create_user(
            user_type=1,
            **validated_data
        )

        NormalUser.objects.create(
            user=user,
            **normal_user_data
        )

        return user


class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'specialist_type',
            'content',
            'work_address',
            'work_phone',
        )


class DoctorCreateSerializer(serializers.ModelSerializer):
    doctor_info = DoctorListSerializer()

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'doctor_info'
        )

    def create(self, validated_data):
        doctor_data = validated_data.pop('doctor_info')
        user = User.objects.create_user(
            user_type=2,
            **validated_data
        )

        Doctor.objects.create(
            user=user,
            **doctor_data
        )

        return user
