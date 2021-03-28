from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.conf import settings
from .serializers import *
from users.models import Doctor, NormalUser, User


class CommentView(APIView):
    permission_classes = (AllowAny,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request):
        doctor_name = request.query_params["username"]
        doctor = User.objects.get(username=doctor_name)
        result = self.queryset.filter(doctor=doctor.doctor_info).values()
        return Response({"data": result})

    def post(self, request):
        doctor_name = request.data["username"]
        comment = request.data["comment"]
        doctor = User.objects.get(username=doctor_name)
        self.queryset.create(doctor=doctor.doctor_info, user=request.user.normal_user_info, comment=comment)
        return Response({"msg": "Added successful"}, status=HTTP_201_CREATED)
