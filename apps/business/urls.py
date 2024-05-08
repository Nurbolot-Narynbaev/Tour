from rest_framework.routers import DefaultRouter

from .views import (
    CompanyViewSet, 
    GuideViewSet,
    )

router = DefaultRouter()
router.register('company', CompanyViewSet)
router.register('guide', GuideViewSet)

urlpatterns = [

]

urlpatterns += router.urls