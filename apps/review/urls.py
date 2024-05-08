from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    SavedTourViewSet,
    TourCommentView,
    RatingView,
    LikeView,
)


router = DefaultRouter()


router.register('saved-tour', SavedTourViewSet, 'saved tour')
router.register('tour-comment', TourCommentView, 'comment')
router.register('tour-rating', RatingView, 'rating')
router.register('tour-like', LikeView, 'like')


urlpatterns = [

]
urlpatterns += router.urls