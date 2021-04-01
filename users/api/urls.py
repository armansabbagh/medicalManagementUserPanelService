from django.urls import path
from .views import *
from rest_framework import routers

app_name = "users"
router = routers.DefaultRouter()
router.register('doctors', DoctorListAPIView)
router.register('normal-user', NormalUserGetAndEditAPIView)

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register-doctor/', DoctorCreateAPIView.as_view()),
    path('register-normal-user/', NormalUserCreateAPIView.as_view()),
    path('register-admin/', AdminCreateAPIView.as_view()),
] + router.urls

