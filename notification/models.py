from django.db import models
from tweet.models import Tweets
from twitteruser.models import MyUser
# Create your models here
 
class Notifications(models.Model):
    tweet = models.ForeignKey(
        Tweets,
         related_name='tweet_notifiation'
         , on_delete=models.CASCADE)
    twitter_user = models.ForeignKey(MyUser,
     related_name='user_notificatons',
      on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    