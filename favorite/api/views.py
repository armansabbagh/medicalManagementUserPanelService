from rest_framework.views import APIView
from favorite.models import Favorite
from .serializer import FavoriteSerializerForDoctor, FavoriteSerializerForUser
from medicalManagementUserPanelService.permisions import DoctorPermission, NormalUserPermission
from rest_framework import viewsets
from rest_framework.response import Response
from users.models import Doctor,User
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
)


class FavoriteListForDoctor(APIView):
    serializer_class = FavoriteSerializerForDoctor
    queryset = Favorite.objects.all()
    permission_classes = (DoctorPermission,)

    def get(self, request):
        data = self.queryset.get(user=request.user.doctor_info)
        FavoriteSerializerForDoctor.to_internal_value(data)


class FavoriteListForUser(APIView):
    serializer_class = FavoriteSerializerForUser
    queryset = Favorite.objects.all()
    permission_classes = (NormalUserPermission,)

    def get(self, request):
        data = self.queryset.filter(user=request.user.normal_user_info).values()
        return Response({"data": data})

    def post(self, request):
        user = request.user
        doctor_username = request.data["username"]
        doctor = User.objects.get(username=doctor_username)
        if not doctor:
            return Response({'msg': "not fouund"}, status=HTTP_404_NOT_FOUND)
        self.queryset.create(user=user.normal_user_info, doctor=doctor.doctor_info)
        return Response({'msg' : "Add successful"},status=HTTP_201_CREATED)