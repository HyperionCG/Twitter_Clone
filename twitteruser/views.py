from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from twitteruser.models import MyUser

# Create your views here.

def index(request):
    userdata = MyUser.objects.all()
    tweetdata = Tweet.objects.all()
    return render(request, 'index.htm', {'userdata': userdata, 'tweetdata': tweetdata})

def user_profile_view(request, id):
    twitteruser = MyUser.objects.get(id=id)
    tweets = Tweet.objects.filter(id=id)
    tweetcount = tweets.count()
    followers =  twitteruser.following.all()
    followercount =  followers.count()

    return render(request, 'userpage.htm', {
        'twitteruser': twitteruser,
        'tweets': tweets,
        'tweetcount': tweetcount,
        'followers': followers,
        'followercount': followercount
        })

def follow_view(request, id):
    user = request.user
    twitteruser = MyUser.objects.get(user=user)
    followuser = MyUser.objects.get(id=id)
    user.following.add(followuser)
    followuser.save()
    return HttpResponseRedirect(reverse(''))

#def unfollow_view(request, id):