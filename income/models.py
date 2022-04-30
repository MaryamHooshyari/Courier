from datetime import datetime

import pytz
from django.db import models

from salary.models import DailySalary


class AbstractIncomeModel(models.Model):
    class Meta:
        abstract = True

    amount = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class TripIncome(AbstractIncomeModel):
    courier = models.ForeignKey('courier.Courier', on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        return f'trip for {self.courier.name}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            daily_obj = DailySalary.objects.get(courier=self.courier, date=self.date)
            daily_obj.amount += self.amount
            daily_obj.save()
        except:
            DailySalary.objects.create(courier=self.courier, date=self.date, amount=self.amount)
        super(TripIncome, self).save()


class IncomeDeduction(AbstractIncomeModel):
    courier = models.ForeignKey('courier.Courier', on_delete=models.CASCADE, related_name='deductions')

    def __str__(self):
        return f'deduction for {self.courier.name}'


class IncomeAddition(AbstractIncomeModel):
    courier = models.ForeignKey('courier.Courier', on_delete=models.CASCADE, related_name='additions')

    def __str__(self):
        return f'addition for {self.courier.name}'
