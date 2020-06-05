from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from twitteruser.models import MyUser
from authentication.forms import LoginForm, SignUpForm

# Create your views here.

def signupview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                )
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    
    form = SignUpForm()
    return render(request, 'generic_form.htm', {'form':form})


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
             username=data['username'],
              password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'generic_form.htm', {'form':form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))