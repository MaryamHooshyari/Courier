from django.db import models


class DailySalary(models.Model):
    courier = models.ForeignKey('courier.Courier', on_delete=models.CASCADE, related_name='daily_salaries')
    date = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.courier.name} in {self.date}'
