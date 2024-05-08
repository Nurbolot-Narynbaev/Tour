from rest_framework.routers import DefaultRouter

from .views import ( 
    TourViewSet,
    Specific_TourViewSet
)

router = DefaultRouter()
router.register("tour", TourViewSet)
router.register("specific-tour",Specific_TourViewSet)

urlpatterns =[
]

urlpatterns += router.urls