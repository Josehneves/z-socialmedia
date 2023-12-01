from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create User Profile Model 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
        related_name="followed_by",symmetrical=False,
        blank=True)
    data_modified = models.DateTimeField(user, auto_now=True)
    join_date = models.DateTimeField(user, auto_now_add=True)
    
    def __str__(self):
        return self.user.username
# Auto create profile and follow user itself when created.
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.userprofile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)
