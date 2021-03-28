from django.urls import path
from .views import *

urlpatterns = [
    path('doctor/', SetVisitTimeForDoctor.as_view()),
    path('user/', SetVisitTimeForUser.as_view()),
    path('visitList/', VisitList.as_view({'get': 'list'})),
]
