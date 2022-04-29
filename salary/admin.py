from django.contrib import admin

from salary.models import DailySalary


@admin.register(DailySalary)
class TripIncomeAdmin(admin.ModelAdmin):
    list_display = ('courier', 'amount', 'date')
    search_fields = ('courier__name', 'amount', 'date')
    list_filter = ('courier', 'date')
