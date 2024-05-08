from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import (
    TourComment,
    TourRating,
    TourLike,
    SavedTour,
)


User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )

    class Meta:
        model = TourComment
        exclude = ('id',)


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = TourLike
        fields = ('user', 'tour')

    def create(self, validated_data):
        user = self.context.get('request').user
        tour = self.context.get('tour')
        like = TourLike.objects.filter(user=user, tour=tour).first()
        if like:
            raise serializers.ValidationError('already liked')
        return super().create(validated_data)

    def unlike(self):
        user = self.context.get('request').user
        tour = self.context.get('tour')
        like = TourLike.objects.filter(user=user, tour=tour).first()
        if like:
            like.delete()
        else:
            raise serializers.ValidationError('not liked yet')
    
    # def validate(self, attrs):
    #     user = self.context.get('request').user
    #     attrs['user'] = user
    #     return attrs


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = TourRating
        fields = ('rating', 'user', 'tour')

    def validate(self, attrs):
        user = self.context.get('request').user
        attrs['user'] = user
        rating = attrs.get('rating') 
        if rating not in (1, 2, 3, 4, 5):
            raise serializers.ValidationError('Incorrect value. The rating should be between 1 and 5.')
        # if rating:
        #     raise serializers.ValidationError('already exists')
        return attrs

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating')
        instance.save()
        return super().update(instance, validated_data)


class SavedTourSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = SavedTour
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        request = self.context.get('request').data
        tour = request.get('tour')
        favorite = SavedTour.objects.filter(user=user, tour=tour).first()
        if not favorite:
            return super().create(validated_data)
        raise serializers.ValidationError('This tour has been saved')

    def del_favorite(self, validated_data):
        user = self.context.get('request').user
        request = self.context.get('request').data
        tour = request.get('tour').slug
        favorite = SavedTour.objects.filter(user=user, tour=tour).first()
        if favorite:
            favorite.delete()
        else:
            raise serializers.ValidationError('This tour has not been saved')