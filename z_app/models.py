from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save

# Create User Profile Model 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
        related_name="followed_by",symmetrical=False,
        blank=True)
    
    def __str__(self):
        return self.user.username
    
class Tweet(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Tweet #{self.id}'

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()

# Auto create profile and follow user itself when created.
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.userprofile.id])
        user_profile.save()
post_save.connect(create_profile, sender=User)

# def create_tweet(sender, instance, created, **kwargs):
#     if created:
#         user_profile = UserProfile(user=instance)
#         user_profile.save()
#         tweet = Tweet(content=instance.text)
#         tweet.save()
# post_save.connect(create_tweet, sender=User)