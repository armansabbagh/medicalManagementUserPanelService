from .views import *
from rest_framework import routers

app_name = "location"
router = routers.DefaultRouter()
router.register('states', StateListAPIView)
router.register('cities', CityListAPIView)

urlpatterns = router.urls

