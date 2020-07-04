from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TwitterUser(AbstractUser):
    user = models.ManyToManyField("self", symmetrical=False)

    #age = models.IntegerField()

    def __str__(self):
        return self.user