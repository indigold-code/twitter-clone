from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Chirp 
# unregister groups
admin.site.unregister(Group)

# mix profile info into user info so not two separate pages
class ProfileInline(admin.StackedInline):
    model = Profile 

# extend user model

class UserAdmin(admin.ModelAdmin):
    model = User

    fields = ["username"]
    inlines = [ProfileInline]

# unregister user 
admin.site.unregister(User)

# reregister user and profile 

admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

admin.site.register(Chirp)




