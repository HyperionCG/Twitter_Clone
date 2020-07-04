from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AbstractUser

from twitteruser.models import TwitterUser
from tweet.models import Tweets
from twitterclone import settings
# Create your views here.

@login_required
def index(request):
    userdata = TwitterUser.objects.all()
    tweetdata = Tweets.objects.all().order_by('-time')
    return render(
        request,
        'index.htm',
        {'userdata': userdata,
        'tweetdata': tweetdata}
        )

def user_profile_view(request, id):
    twitteruser = TwitterUser.objects.get(id=id)
    tweets = Tweets.objects.filter(id=id).order_by('-date')
    tweetcount = tweets.count()
    followers =  twitteruser.user.all()
    followercount =  followers.count()

    return render(request, 'profilepage.htm', {
        'twitteruser': twitteruser,
        'tweets': tweets,
        'tweetcount': tweetcount,
        'followers': followers,
        'followercount': followercount
        })

def follow_view(request, id):
    user = request.user
    twitteruser = TwitterUser.objects.get(user=user)
    followuser = TwitterUser.objects.get(id=id)
    user.user.add(followuser)
    followuser.save()
    return HttpResponseRedirect(reverse('profile', args={id, }))

def unfollow_view(request, id):
    user = request.user
    twitteruser = TwitterUser.objects.get(user=user)
    followuser = TwitterUser.objects.get(id=id)
    user.user.add(followuser)
    followuser.save()
    return HttpResponseRedirect(reverse('profile', args={id, }))
    