from rest_framework.routers import DefaultRouter

from common.views import AuthorizationViewSet, PatientViewSet

router = DefaultRouter()

router.register(prefix='login', basename='login', viewset=AuthorizationViewSet)
router.register(prefix='patients', basename='patients', viewset=PatientViewSet)

urlpatterns = router.urls
