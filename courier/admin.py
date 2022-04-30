from django.contrib import admin

from courier.models import Courier


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
