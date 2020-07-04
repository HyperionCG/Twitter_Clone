from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.models import Tweets
from tweet.forms import TweetForm
from notification.models import Notifications
from twitteruser.models import TwitterUser


# Create your views here.

def notifications_view(request, id):
    pingeduser = TwitterUser.objects.filter(id=id).first()
    data = Notifications.objects.filter(user=pingeduser)
    for notice in data:
        notice.delete()
    return render(request, 'notifications.htm', {'data': data})