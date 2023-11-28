from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
# Create User Profile Model 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
        related_name="followed_by",symmetrical=False,
        blank=True)
    
    def __str__(self):
        return self.user.username
=======
# Create your models here.

from django.db import models
from django.conf import settings

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
>>>>>>> b67d6d7959c94ca1a83f8d5defd1b346a5f20740
