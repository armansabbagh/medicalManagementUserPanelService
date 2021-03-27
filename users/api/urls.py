from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register-doctor/', DoctorCreateAPIView.as_view()),
    path('register-normal-user/', NormalUserCreateAPIView.as_view()),
    path('register-admin/', AdminCreateAPIView.as_view()),
]
