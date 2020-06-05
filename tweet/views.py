from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweets
from tweet.forms import TweetForm
from notification.models import Notifications

# Create your views here.

@login_required
def index(request):
    user = request.user
    twitteruser = MyUser.objects.get(user=user)
    notifications = Notifications.objects.filter()
    return render(request, 'index.html')
