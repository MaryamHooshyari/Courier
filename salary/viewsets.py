import datetime

from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from courier.models import Courier
from salary.filtersets import DailySalaryFilterSet
from salary.models import DailySalary
from salary.serializers import DailySalarySerializer


class DailySalaryViewSet(viewsets.ModelViewSet):
    queryset = DailySalary.objects.all()
    serializer_class = DailySalarySerializer
    filterset_class = DailySalaryFilterSet

    @action(methods=['get'], detail=False, url_path='weeklies', url_name='weeklies')
    def weekly_salary(self, request):
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        delta = datetime.timedelta(days=1)
        salary = {}
        try:
            for courier in Courier.objects.all():
                salary[courier] = []
                while from_date <= to_date:
                    if from_date.isoweekday() == 6:
                        salary[courier].append((from_date, DailySalary.objects.filter(date__gte=from_date,
                                                                                      date__lt=from_date + datetime.timedelta(
                                                                                          days=7)).aggregate(weekly_salary=Sum('amount'))))
                    print(from_date.isoweekday())
                    from_date += delta
            return Response(salary)
        except Exception as e:
            return Response({'error': 'something went wrong!', 'exception': e})
