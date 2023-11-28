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

    