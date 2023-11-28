# z_app views
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentFormfrom django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def comment_list(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    comments = tweet.comments.all()
    return render(request, 'z_app/comment_list.html', {'comments': comments, 'tweet': tweet})

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
