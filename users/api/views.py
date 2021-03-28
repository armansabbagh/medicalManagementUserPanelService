from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.conf import settings
from .serializers import *
from users.models import Doctor, NormalUser
from rest_framework_simplejwt.tokens import RefreshToken
from medicalManagementUserPanelService.permisions import DoctorPermission

class DoctorCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Doctor.objects.all()
    serializer_class = DoctorCreateSerializer

    def perform_create(self, serializer):
        serializer.save()


class NormalUserCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = NormalUser.objects.all()
    serializer_class = NormalUserCreateSerializer

    def perform_create(self, serializer):
        serializer.save()


class AdminCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AdminCreateSerializer

    def perform_create(self, serializer):
        serializer.save()


class LoginAPIView(APIView):
    # permission_classes = (DoctorPermission,)
    permission_classes = (AllowAny,)
    queryset = Doctor.objects.all()
    serializer_class = LoginSerializer


    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        if username is None or password is None:
            return Response({
                'error': 'Please provide both username and password',
                'message': 'Please provide both username and password'
            }, status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
        users_types = {0: 'admin', 1: 'normal_user', 2: 'doctor'}
        user_type = int(request.data['user_type'])
        if user_type and user_type == user.user_type:
            # token, _ = Token.objects.get_or_create(user=user)
            token = RefreshToken.for_user(user)
            return Response({'state': 'successful', 'token': str(token.access_token)}, status=HTTP_200_OK)
        else:
            return Response({
                'error': 'invalid type',
                'message': 'user type should be doctor or normal_user'
            }, status=HTTP_400_BAD_REQUEST)
