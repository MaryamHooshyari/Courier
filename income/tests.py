from datetime import datetime

import pytz
from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status

from courier.models import Courier
from income.viewsets import TripIncomeViewSet, IncomeDeductionViewSet
from salary.models import DailySalary


class TripIncomeTest(TestCase):
    def setUp(self):
        self.courier = Courier.objects.create(name='Miriam')

    # url test
    def test_trip_income_urls_are_resolved(self):
        url = reverse('trips-list')
        self.assertEqual(resolve(url).func.cls, TripIncomeViewSet)

    def test_trip_income_create_daily_salary(self):
        data = {'courier': self.courier.pk, 'amount': 15, 'date': datetime.now(pytz.timezone('Asia/Tehran')).date(),
                'time': datetime.now(pytz.timezone('Asia/Tehran')).time()}
        response = self.client.post(reverse('trips-list'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.daily = DailySalary.objects.all().last()
        self.assertEqual(self.daily.courier.pk, response.data['courier'])
        self.assertEqual(self.daily.amount, response.data['amount'])
        self.assertEqual(str(self.daily.date), response.data['date'])


class IncomeDeductionTest(TestCase):
    def setUp(self):
        self.courier = Courier.objects.create(name='Miriam')

    # url test
    def test_income_deduction_urls_are_resolved(self):
        url = reverse('deductions-list')
        self.assertEqual(resolve(url).func.cls, IncomeDeductionViewSet)

    def test_income_deduction_create_daily_salary(self):
        data = {'courier': self.courier.pk, 'amount': 15, 'date': datetime.now(pytz.timezone('Asia/Tehran')).date(),
                'time': datetime.now(pytz.timezone('Asia/Tehran')).time()}
        response = self.client.post(reverse('deductions-list'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.daily = DailySalary.objects.all().last()
        self.assertEqual(self.daily.courier.pk, response.data['courier'])
        self.assertEqual(self.daily.amount, -response.data['amount'])
        self.assertEqual(str(self.daily.date), response.data['date'])
