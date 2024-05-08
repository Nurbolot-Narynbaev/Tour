from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model

User = get_user_model()

class Company(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    adress = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    working_since = models.DateField
    profile_created_at = models.CharField(max_length=20)
    slug = models.CharField(max_length=25)
    


    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
    )

    def str(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Guide(models.Model):
    first_name = models.CharField(max_length=20)
    user = models.ForeignKey
    last_name = models.CharField(max_length=20)
    company = models.ForeignKey
    image = models.CharField(max_length=20)
    about = models.CharField(max_length=100)
    age = models.CharField(max_length=20)
    slug = models.CharField(max_length=25)


    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
    )

    def str(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Guide'
        verbose_name_plural = 'Guides'