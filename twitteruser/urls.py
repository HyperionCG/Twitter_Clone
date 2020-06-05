from django.urls import path
from twitteruser import views

urlpatterns = [ 
    path('user/', views.index, name = 'home'),
    path('profile/<int:id>/', views.user_profile_view, name = 'userpage'),
    path('follow/<int:id>/', views.follow_view, name = 'follow'),
    #path('unfollow/<int:id>', views.unfollow_view, name = 'unfollow'),
]