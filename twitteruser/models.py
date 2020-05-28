from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    user = models.CharField(max_length=50, null=True, blank=True)
    #age = models.IntegerField()

    def __str__(self):
        return self.user