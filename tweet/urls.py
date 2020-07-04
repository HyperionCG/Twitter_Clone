from django.urls import path
from tweet import views

urlpatterns = [ 
    path('tweet/<int:id>/', views.tweet_view, name = 'tweet'),
    path('add_tweet/', views.add_tweet, name = 'add_tweet'),
    ]