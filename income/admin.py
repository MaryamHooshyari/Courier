from django.contrib import admin

from income.models import TripIncome, IncomeDeduction, IncomeAddition


@admin.register(TripIncome)
class TripIncomeAdmin(admin.ModelAdmin):
    list_display = ('courier', 'amount', 'date', 'time')
    search_fields = ('courier__name', 'amount', 'date')
    list_filter = ('courier', 'date')


@admin.register(IncomeDeduction)
class IncomeDeductionAdmin(admin.ModelAdmin):
    list_display = ('courier', 'amount', 'date', 'time')
    search_fields = ('courier__name', 'amount', 'date')
    list_filter = ('courier', 'date')


@admin.register(IncomeAddition)
class IncomeAdditionAdmin(admin.ModelAdmin):
    list_display = ('courier', 'amount', 'date', 'time')
    search_fields = ('courier__name', 'amount', 'date')
    list_filter = ('courier', 'date')
