from django.shortcuts import render, redirect
from django.contrib.auth.admin import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import tweettable
from .forms import register_form, twitter_form

@login_required
def index(request):
    username = None
    AllTweets = tweettable.objects.all()
    SelfTweet = 'Tweets not available.'
    LikedTweet = 'Tweets not available.'
    try:
        username = User.objects.get(username=request.user.username)
        SelfTweet = tweettable.objects.filter(user=request.user)
        LikedTweet = tweettable.objects.filter(is_liked=True, user=request.user)

    except User.DoesNotExist:
        return render(request,'webapp/index.html',{'SelfTweet':SelfTweet,'LikedTweet':LikedTweet,'AllTweets':AllTweets})

    return render(request, 'webapp/index.html',{'SelfTweet': SelfTweet, 'LikedTweet': LikedTweet, 'AllTweets': AllTweets, 'username':username})

def register_user(request):

    if request.method == 'POST':

        form = register_form(request.POST)

        if form.is_valid():

            user1 = form.save(commit=False)
            user1.set_password(user1.password)
            user1.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request,user)
                return redirect('index')
    else:

        form = register_form()

    return render(request, 'webapp/register.html',{'form':form})

@login_required
def twitter(request):

    if request.method == 'POST':
        form = twitter_form(request.POST)
        form.instance.user = request.user

        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('index')
    else:
        form = twitter_form()
    return render(request, 'webapp/twitter.html', {'form': form})

