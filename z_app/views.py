# z_app views
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm
from .models import Tweet
from .forms import TweetForm

# Create your views here.
def home(request):
    tweets = Tweet.objects.all()
    return render(request, 'home.html', {'tweets': tweets})

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
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.save()
            return redirect('tweet_detail', pk=tweet.pk)
    else:
        form = TweetForm()
    return render(request, 'tweet_new.html', {'form': form})

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
    return render(request, 'tweet_edit.html', {'form': form})

def tweet_delete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    tweet.delete()
    return redirect('tweet_list')

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
    return render(request, 'z_app/comment_form.html', {'form': form, 'tweet': tweet})

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
    return render(request, 'z_app/comment_form.html', {'form': form, 'tweet': tweet})

def comment_delete(request, tweet_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('comment_list', tweet_id=tweet_id)
