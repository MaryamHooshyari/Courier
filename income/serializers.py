from rest_framework import serializers

from income.models import TripIncome, IncomeDeduction, IncomeAddition


class TripIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripIncome
        fields = '__all__'


class IncomeDeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeDeduction
        fields = '__all__'


class IncomeAdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeAddition
        fields = '__all__'
