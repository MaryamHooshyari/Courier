from rest_framework import viewsets

from salary.models import DailySalary
from salary.serializers import DailySalarySerializer


class DailySalaryViewSet(viewsets.ModelViewSet):
    queryset = DailySalary.objects.all()
    serializer_class = DailySalarySerializer
