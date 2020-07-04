from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

# Create your models here.
class Tweets(models.Model):
    text = models.CharField(max_length=140)
    time = models.DateTimeField(timezone.now)
    likes = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    author = models.ForeignKey(TwitterUser, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
