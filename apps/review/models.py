from django.db import models
from django.contrib.auth import get_user_model
# from django.urls import reverse


from apps.tour.models import Specific_Tour


User = get_user_model()


class TourComment(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    tour = models.ForeignKey(
        to=Specific_Tour,
        on_delete=models.CASCADE,
        related_name='tours_comments'
    )
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment from {self.user.username} to {self.tour.title}'


class TourRating(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE =5
    RATING_CHOICES = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5')
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, blank=True, null=True)
    tour = models.ForeignKey(
        to=Specific_Tour,
        on_delete=models.CASCADE,
        related_name='tours_ratings'
    )

    def __str__(self) -> str:
        return f'{self.rating} points to {self.tour.title}'
    
    class Meta:
        unique_together = ['user', 'tour', 'rating']


class TourLike(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='likes',
        null=True
    )
    tour = models.ForeignKey(
        to=Specific_Tour,
        on_delete=models.CASCADE,
        related_name='tours_likes'
    )
    # book_id = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'Liked by {self.user.username}'
    

class SavedTour(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    tour = models.ForeignKey(
        to=Specific_Tour,
        on_delete=models.CASCADE,
    )