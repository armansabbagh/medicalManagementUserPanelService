from django.urls import path
from .views import *

urlpatterns = [
    path('doctor/', FavoriteListForDoctor.as_view()),
    path('user/', FavoriteListForUser.as_view()),
]
