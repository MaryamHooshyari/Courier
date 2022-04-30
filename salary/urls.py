from rest_framework import routers

from salary.viewsets import DailySalaryViewSet

router = routers.SimpleRouter()

router.register('dailies', DailySalaryViewSet, basename='dailies')

urlpatterns = router.urls
