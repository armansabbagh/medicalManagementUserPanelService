from django.urls import path
from .views import *

urlpatterns = [
    path('', CommentView.as_view()),
]
