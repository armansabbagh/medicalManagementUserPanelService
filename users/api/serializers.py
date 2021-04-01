from rest_framework import serializers
from users.models import *
from rest_framework_simplejwt.tokens import RefreshToken


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
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = NormalUser
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'national_code',
            'phone',
            'home_phone',
            'address',
            'disease',
            'disease_detail'
        ]

    def get_first_name(self, instance):
        return instance.user.first_name

    def get_last_name(self, instance):
        return instance.user.last_name


class NormalUserCreateSerializer(serializers.ModelSerializer):
    normal_user_info = NormalUserDetailSerializer()
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'normal_user_info',
            'token'
        ]
        read_only_fields = ['token']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def get_token(self, instance):
        return str(RefreshToken.for_user(instance))

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
    name = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ['name']

    def get_name(self, instance):
        return instance.user.first_name + ' ' + instance.user.last_name

    def get_city(self, instance):
        return instance.city.name


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'specialist_type',
            'content',
            'city',
            'work_address',
            'work_phone',
            'supervisor_number',
            'degree'
        )


class DoctorCreateSerializer(serializers.ModelSerializer):
    doctor_info = DoctorSerializer()
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'doctor_info',
            'token'
        )
        read_only_fields = ['token']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def get_token(self, instance):
        return str(RefreshToken.for_user(instance))

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

    # def to_representation(self, obj):
    #     ret = super(DoctorCreateSerializer, self).to_representation(obj)
    #     ret.pop('password')
    #     return ret


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'user_type')

    def validate(self, attrs):
        username = attrs.get("username", "")
        password = attrs.get("password", "")
        # if username is None or password is None:
        #     raise {
        #         'error': 'Please provide both username and password',
        #         'message': 'Please provide both username and password'
        #     }
        # if not user:
        #     raise
        #
        # user = auth.authenticate(username=username, password=password)
        # if user:
