from django.shortcuts import render
from django.http import HttpResponse
from .models import tweet, useradd, comment
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm, TweetForm, CommentForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        form = TweetForm(request.POST or None, request.FILES or None)
        userses = request.user
        if form.is_valid():
            tfrom = request.user.username
            fetch_obj= useradd.objects.filter(username=tfrom)[0]
            tweetfrom = fetch_obj
            text  = form.cleaned_data['text']
            tweetto = form.cleaned_data['tweetto']
            '''if(request.FILES.items()):
                smiley = request.FILES['smiley']
            else:
                smiley=None'''
            temp_obj = tweet()
            temp_obj.text = text
            temp_obj.tweetfrom = tweetfrom
            temp_obj.save()
            for item in tweetto:
                temp_obj.tweetto.add(item)
            temp_obj.save()
            form = TweetForm(None)


        context = {
            "form": form,
            "all_tweets" : tweet.objects.all(),
            "user1":useradd.objects.get(username=request.user.username),
            "comment":comment.objects.all()
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'login.html')

def register(request):
    if(not request.user.is_authenticated):
        form = UserForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            usern = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            usern.set_password(password)
            usern.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    form = TweetForm(None)
                    userses = request.user
                    context={
                        "form":form,
                        "all_tweets": tweet.objects.all(),
                        "user1":useradd.objects.get(username=request.user.username)
                    }
                    return render(request, 'index.html', context)
        context = {
            "form": form
        }
        return render(request, 'register.html', context)
    else:
        form = TweetForm(None)
        userses = request.user
        context = {
            "form": form,
            "all_tweets": tweet.objects.all(),
            "user1":useradd.objects.get(username=userses.username)
        }
        return render(request, 'index.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                form = TweetForm(None)
                context = {
                    "form": form,
                    "all_tweets": tweet.objects.all(),
                    "user1":useradd.objects.get(username=request.user.username)
                }
                return render(request, 'index.html', context)
            else:
                return render(request, 'login.html', {"error_message":"Your account has been suspended."})
        else:
            return render(request, 'login.html', {"error_message": "Invalid Login Details."})
    elif request.user.is_authenticated:
        form = TweetForm(None)
        context = {
            "form": form,
            "all_tweets": tweet.objects.all(),
            "user1":useradd.objects.get(username=request.user.username)
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return render(request, 'login.html')

def commentadd(request, tweet_id):
    form = CommentForm(request.POST or None)
    message=""
    if form.is_valid():
        newcomment = form.save(commit=False)
        cmfrom = request.user.username
        fetch_obj = useradd.objects.filter(username=cmfrom)[0]
        newcomment.commentfrom = fetch_obj
        newcomment.commenton = tweet.objects.get(pk=tweet_id)
        newcomment.save()
        message="Successfully added a comment"
    context = {
        'form':form,
        "user1": useradd.objects.get(username=request.user.username),
        "message":message
    }
    return render(request, 'comment.html', context)





