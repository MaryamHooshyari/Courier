from django.db import transaction
from rest_framework import viewsets

from income.models import TripIncome, IncomeDeduction, IncomeAddition
from income.serializers import TripIncomeSerializer, IncomeDeductionSerializer, IncomeAdditionSerializer
from salary.models import DailySalary


class TripIncomeViewSet(viewsets.ModelViewSet):
    queryset = TripIncome.objects.all()
    serializer_class = TripIncomeSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()
            instance = serializer.instance
            try:
                daily_obj = DailySalary.objects.get(courier=instance.courier, date=instance.date)
                daily_obj.amount += instance.amount
                daily_obj.save()
            except:
                DailySalary.objects.create(courier=instance.courier, date=instance.date, amount=instance.amount)


class IncomeDeductionViewSet(viewsets.ModelViewSet):
    queryset = IncomeDeduction.objects.all()
    serializer_class = IncomeDeductionSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()
            instance = serializer.instance
            try:
                daily_obj = DailySalary.objects.get(courier=instance.courier, date=instance.date)
                daily_obj.amount -= instance.amount
                daily_obj.save()
            except:
                DailySalary.objects.create(courier=instance.courier, date=instance.date, amount=-instance.amount)


class IncomeAdditionViewSet(viewsets.ModelViewSet):
    queryset = IncomeAddition.objects.all()
    serializer_class = IncomeAdditionSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()
            instance = serializer.instance
            try:
                daily_obj = DailySalary.objects.get(courier=instance.courier, date=instance.date)
                daily_obj.amount += instance.amount
                daily_obj.save()
            except:
                DailySalary.objects.create(courier=instance.courier, date=instance.date, amount=instance.amount)
