from django import forms

from tweet.models import Tweets

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweets
        fields = ['text']