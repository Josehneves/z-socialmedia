# z_app views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, TweetForm, CommentForm
from .models import UserProfile, Tweet, Comment


# Create your views here.
def home(request):
    tweets = Tweet.objects.all()
    return render(request, 'home.html', {'tweets': tweets, 'user': request.user})

def profiles(request):
    if request.user.is_authenticated:
        profile_list = UserProfile.objects.exclude(user=request.user)
        return render(request, 'profiles.html', {"Profiles":profile_list})
    else:
        messages.success(request,"Please create an account to view this page or login if you have an existing account with us.")
        return redirect('home')

def profile(request,pk):
    if request.user.is_authenticated:  
        profile = UserProfile.objects.get(user_id=pk)
        tweets = Tweet.objects.filter(user_id=pk)
        return render(request, 'profile.html',{"profile":profile, "tweets":tweets})
    else:
        messages.success(request,"Please create an account to view this page or login if you have an existing account with us.")
        return redirect('home')
    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Successful login.")
            return redirect('home')
        else:
            messages.success(request,"Login failed.")
            return redirect('login')
    else:
        return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"User logged out.")
    return redirect('login')

def register_newuser(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Successfully created an account.")
            return redirect('home')
        
    return render(request, 'register.html', {'form':form})

def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweet_list.html', {'tweets': tweets})

def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    comments = tweet.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.tweet = tweet
            new_comment.user = request.user
            new_comment.save()
            return redirect('tweet_detail', pk=tweet.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'tweet_detail.html', {
        'tweet': tweet,
        'comments': comments,
        'form': comment_form
    })

def tweet_new(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_detail', pk=tweet.pk)
    else:
        form = TweetForm()
    return render(request, 'tweet_new.html', {'form': form})

def tweet_edit(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_detail', pk=tweet.pk)
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_edit.html', {'form': form})

def tweet_delete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    tweet.delete()
    return redirect('home')

def comment_list(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    comments = tweet.comments.all()
    return render(request, 'z_app/templates/comment_list.html', {'comments': comments, 'tweet': tweet})

def comment_create(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.tweet = tweet
            comment.user = request.user
            comment.save()
            return redirect('comment_detail', tweet_id=tweet_id, comment_id=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'z_app/templates/comment_form.html', {'form': form, 'tweet': tweet})

def comment_detail(request, tweet_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'z_app/templates/comment_detail.html', {'comment': comment})

def comment_update(request, tweet_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', tweet_id=tweet_id, comment_id=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'z_app/templates/comment_form.html', {'form': form, 'tweet': tweet})

def comment_delete(request, tweet_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('z_app/templates/comment_list', tweet_id=tweet_id)
