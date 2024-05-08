from rest_framework.permissions import (
    IsAuthenticated,
)

from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import(
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework import mixins

from apps.account.permissions import IsOwner 
from apps.tour.models import Tour

from .serializers import (
    RatingSerializer,
    CommentSerializer,
    LikeSerializer,
    SavedTourSerializer
)
from .models import (
    TourComment, 
    TourLike,
    TourRating,
    SavedTour
)


class SavedTourViewSet(mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = SavedTour.objects.all()
    serializer_class = SavedTourSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'save' and self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        if self.action == 'save' and self.request.method =='DELETE':
            self.permission_classes = [IsOwner]
        if self.action == 'list':
            self.permission_classes = [IsOwner]
        return super().get_permissions()

    def save(self, request, pk=None):
        tour = self.get_object().get('slug')
        serializer = SavedTourSerializer(
            data=request.data, 
            context={
                'request':request,
                'tour':tour
            })
        if serializer.is_valid(raise_exception=True):
            if request.method == 'POST':
                serializer.save(user=request.user)
                return Response('This tour has been saved')
            if request.method == 'DELETE':
                        serializer.del_favorite()
                        return Response('This tour has been removed from savings')


class TourCommentView(mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    queryset = TourComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer): 
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class RatingView(mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    queryset = TourRating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class LikeView(mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    serializer_class = LikeSerializer
    queryset = TourLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'like' and self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        if self.action == 'like' and self.request.method =='DELETE':
            self.permission_classes = [IsOwner]
        return super().get_permissions()
    
    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['request'] = self.request
    #     return context

    def like(self, request, pk=None):
        tour = self.get_object()
        serializer = LikeSerializer(
            data=request.data, 
            context={
                'request':request,
                'tour': tour
            })
        if serializer.is_valid(raise_exception=True):
            if request.method == 'POST':
                serializer.save(user=request.user)
                return Response('liked!')
            if request.method == 'DELETE':
                serializer.unlike()
                return Response('unliked!')