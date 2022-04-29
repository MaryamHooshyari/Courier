from rest_framework import viewsets

from income.models import TripIncome, IncomeDeduction, IncomeAddition
from income.serializers import TripIncomeSerializer, IncomeDeductionSerializer, IncomeAdditionSerializer


class TripIncomeViewSet(viewsets.ModelViewSet):
    queryset = TripIncome.objects.all()
    serializer_class = TripIncomeSerializer


class IncomeDeductionViewSet(viewsets.ModelViewSet):
    queryset = IncomeDeduction.objects.all()
    serializer_class = IncomeDeductionSerializer


class IncomeAdditionViewSet(viewsets.ModelViewSet):
    queryset = IncomeAddition.objects.all()
    serializer_class = IncomeAdditionSerializer
