from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweets
from tweet.forms import TweetForm
from notification.models import Notifications
from twitteruser.models import TwitterUser
import re

# Create your views here.
@login_required
def add_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweets.objects.create(
                text=data['text'],
                author=request.user,  
            )
            all_users = re.look(r'@(\w+)', data['text'])
            for pinged in all_users:
                 Notifications.objects.create(
                    pinged_user = TwitterUser.objects.get(username=pinged),
                    text = text,
                    )
            return HttpResponseRedirect(reverse('homepage'))
    
    form = TweetForm()
    return render(request, 'addtweet.htm' , {"form": form})    

@login_required
def tweet_view(request, id):
    tweets = Tweets.objects.get(id=id)
    return render(request, 'tweet_page.htm', {'tweets':tweets})
