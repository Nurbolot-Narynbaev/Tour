from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from apps.tour.models import Tour

from django.contrib.auth import get_user_model

User = get_user_model()
class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('finished', 'Finished')
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        related_name='orders'
    )
    tour = models.ManyToManyField(
        to=Tour,
        through='Order_Items',
    )
    order_id = models.CharField(max_length=58, blank=True)
    total_sum = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Order # {self.order_id}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.order_id:
            self.order_id = str(self.user.username) + str(self.created_at)[11:19]  #
        return self.order_id
    
    class Meta:
        verbose_name = 'Tour order'
        verbose_name_plural = 'Tour orders'


class Order_Items(models.Model):
    order = models.ForeignKey(
        to=Order,
        on_delete=models.RESTRICT, 
        related_name='items'  #
    )
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.RESTRICT,
        related_name='items'   #
    )
    tour_num = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Basket item'
        verbose_name_plural = 'Basket items'