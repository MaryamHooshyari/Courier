from rest_framework import serializers

from salary.models import DailySalary


class DailySalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySalary
        fields = '__all__'
