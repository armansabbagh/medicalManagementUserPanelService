from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import VisitSerializerForDoctor, VisitListSerializer, VisitSerializerForUser
from visits.models import VisitTime
from rest_framework.permissions import AllowAny
from medicalManagementUserPanelService.permisions import DoctorPermission, NormalUserPermission
import datetime
from rest_framework import viewsets


class SetVisitTimeForDoctor(APIView):
    serializer_class = VisitSerializerForDoctor
    queryset = VisitTime.objects.all()
    permission_classes = (DoctorPermission,)

    def post(self, request):
        user = request.user
        date = request.data["date"]
        start_time = datetime.time.fromisoformat(request.data["time"])
        end_time = datetime.time.fromisoformat(request.data["endTime"])
        tempTime = start_time

        while tempTime < end_time:
            sec = int(request.data["duration"]) * 60
            tempTime = self.addSecs(tm=tempTime, secs=sec)
            self.queryset.create(date=date, doctor=user.doctor_info, time=tempTime.__str__())

        return Response({'status': 'success'})

    def addSecs(self, tm, secs):
        fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
        fulldate = fulldate + datetime.timedelta(seconds=secs)
        return fulldate.time()


class SetVisitTimeForUser(APIView):
    serializer_class = VisitListSerializer
    queryset = VisitTime.objects.all()
    permission_classes = (NormalUserPermission,)

    def post(self, request):
        user = request.user
        time_id = request.data["visit_id"]
        selected_time = self.queryset.get(id=time_id)
        selected_time.patient = user.normal_user_info
        selected_time.save()
        return Response({"msg": "Update SuccessFul"})

    def get(self, request):
        data = self.queryset.filter(patient=request.user.normal_user_info).values()

        return Response(data)


class VisitList(viewsets.ModelViewSet):
    serializer_class = VisitListSerializer
    queryset = VisitTime.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = [SearchFilter]
    search_fields = ['doctor__user__username']

    def get(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer_class()(qs)
        return Response({"data": serializer.data})
