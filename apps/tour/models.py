from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model

User = get_user_model()
    

class Tour(models.Model):
    title = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    days = models.CharField(max_length=20)
    company = models.ForeignKey
    user = models.ForeignKey
    slug = models.CharField(max_length=25)
    


    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
    )

    def str(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'


class Tour_Image(models.Model):
    tour = models.ForeignKey
    user = models.ForeignKey
    image = models.ImageField


    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
    )

    def str(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Tour_Images'
        verbose_name_plural = 'Tour_Images'


class Specific_Tour(models.Model):
    max_people = models.CharField(max_length=20)
    user = models.ForeignKey
    min_age = models.CharField(max_length=20)
    guide = models.ForeignKey
    date = models.DateField(max_length=20)
    slug = models.CharField(max_length=25)


    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
    )

    def str(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Specific_Tour'
        verbose_name_plural = 'Specific_Tours'