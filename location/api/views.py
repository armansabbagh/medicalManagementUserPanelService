from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import mixins


class CityListAPIView(viewsets.GenericViewSet,
                      mixins.ListModelMixin, mixins.RetrieveModelMixin):
    model = City
    serializer_class = CitySerializer
    queryset = City.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        if self.request.GET.get('state', ''):
            return City.objects.filter(state=self.request.GET.get('state'))
        return City.objects.all()


class StateListAPIView(viewsets.GenericViewSet,
                       mixins.ListModelMixin, mixins.RetrieveModelMixin):
    model = State
    serializer_class = StateSerializer
    queryset = State.objects.all()
    permission_classes = [AllowAny]

