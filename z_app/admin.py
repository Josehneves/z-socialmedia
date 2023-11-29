from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import UserProfile

# Unregister models here.
admin.site.unregister(Group)
admin.site.unregister(User)

# Register models here.
# Extend User model

class MergeUserProfile(admin.StackedInline):
    model = UserProfile
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [MergeUserProfile]

admin.site.register(User, UserAdmin)


