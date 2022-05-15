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
        from_date_ = request.GET.get('from_date').split('-')
        from_date = datetime.date(int(from_date_[0]), int(from_date_[1]), int(from_date_[2]))
        to_date_ = request.GET.get('to_date').split('-')
        to_date = datetime.date(int(to_date_[0]), int(to_date_[1]), int(to_date_[2]))
        delta = datetime.timedelta(days=1)
        salary = {}
        try:
            for courier in Courier.objects.all():  # TODO: add value+annotate in query to group-by instead of this "for"
                salary[courier.name] = []
                from_date = datetime.date(int(from_date_[0]), int(from_date_[1]), int(from_date_[2]))
                while from_date <= to_date:
                    if from_date.isoweekday() == 6:
                        salary[courier.name].append((from_date, DailySalary.objects.filter(courier=courier, date__gte=from_date,
                                                                                           date__lt=from_date + datetime.timedelta(
                                                                                               days=7)).aggregate(weekly_salary=Sum('amount'))))
                    from_date += delta
            return Response(salary)
        except Exception as e:
            print(e)
            return Response(exception=e, data={'error': 'something went wrong!'})
