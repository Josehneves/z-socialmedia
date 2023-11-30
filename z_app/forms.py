from django import forms
from .models import Tweet
from .models import Comment

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('user', 'content',)
        widgets = {
            'user': forms.HiddenInput(),
            'content': forms.Textarea(attrs={'placeholder': 'Write your tweet here'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Write your comment here'}),
        }