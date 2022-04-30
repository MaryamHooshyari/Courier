from rest_framework import routers

from courier.viewsets import CourierViewSet

router = routers.SimpleRouter()

router.register('couriers', CourierViewSet, basename='couriers')

urlpatterns = router.urls
