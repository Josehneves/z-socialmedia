from django.contrib import admin
from django.contrib.auth.models import Group, User

# Unregister models here.
admin.site.unregister(Group)
admin.site.unregister(User)

# Register models here.
# Extend User model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
admin.site.register(User, UserAdmin)
