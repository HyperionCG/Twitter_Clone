from django.db import models
from tweet.models import Tweets
from twitteruser.models import TwitterUser
# Create your models here
 
class Notifications(models.Model):
    tweet = models.ForeignKey(
      Tweets,
      related_name='tweet_notifiation',
      on_delete=models.CASCADE
      )
    pinged_user = models.ForeignKey(
      TwitterUser,
      related_name='user_notificatons',
      on_delete=models.CASCADE
      )
    received = models.BooleanField(default=False)
    