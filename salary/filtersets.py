import django_filters
from django.db.models import Q

from salary.models import DailySalary


class DailySalaryFilterSet(django_filters.FilterSet):
    order_by = django_filters.OrderingFilter(label='Custom Ordering',
                                             fields=('amount', 'date', 'time', 'created', 'modified'))
    search = django_filters.CharFilter(method='searching', label='Search')

    class Meta:
        model = DailySalary
        fields = '__all__'

    def searching(self, queryset, name, value):
        return DailySalary.objects.filter(Q(courier__name__icontains=value) |
                                          Q(amount__iexact=value) |
                                          Q(date=value) |
                                          Q(date__month=value) |
                                          Q(date__year=value))
