from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm

def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'zsocialmedia/templates/tweet_list.html', {'tweets': tweets})

def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    return render(request, 'zsocialmedia/templates/tweet_detail.html', {'tweet': tweet})

def tweet_new(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.save()
            return redirect('tweet_detail', pk=tweet.pk)
    else:
        form = TweetForm()
    return render(request, 'zsocialmedia/templates/tweet_edit.html', {'form': form})

def tweet_edit(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == "POST":
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.save()
            return redirect('tweet_detail', pk=tweet.pk)
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'zsocialmedia/templates/tweet_edit.html', {'form': form})

def tweet_delete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    tweet.delete()
    return redirect('tweet_list')
