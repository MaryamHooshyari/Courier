from rest_framework import routers

from income.viewsets import TripIncomeViewSet, IncomeDeductionViewSet, IncomeAdditionViewSet

router = routers.SimpleRouter()

router.register('trips', TripIncomeViewSet, basename='trips')
router.register('deductions', IncomeDeductionViewSet, basename='deductions')
router.register('additions', IncomeAdditionViewSet, basename='additions')

urlpatterns = router.urls
