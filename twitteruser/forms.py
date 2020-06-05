from django import forms
from twitteruser.models import MyUser

class MyUserForm(form.ModelForm):
    username = forms.CharField(max_length=50, request=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = MyUser
        fields = ['username','password']