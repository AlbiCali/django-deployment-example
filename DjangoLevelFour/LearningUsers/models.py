from django.db import models
from django.contrib.auth.models import User


class UserProfileInfoClass(models.Model):
    #to add more attributes
    user=models.OneToOneField(User)

    #additional classes
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


# Create your models here.
