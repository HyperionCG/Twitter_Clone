from django.db import models
from django.utils import timezone

# Create your models here.
class Tweets(models.Model):
    text = models.CharField(max_length=280)
    time = models.DateTimeField(timezone.now)
    likes = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)

    def __str__(self):
        return self.text
