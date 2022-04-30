from rest_framework import viewsets

from courier.models import Courier
from courier.serializers import CourierSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
