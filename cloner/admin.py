from django.contrib import admin
from django.contrib.auth.models import Group, User

# unregister groups
admin.site.unregister(Group)



# extend user model

class UserAdmin(admin.ModelAdmin):
    model = User

    fields = ["username"]

# unregister user 
admin.site.unregister(User)

# reregister user

admin.site.register(User, UserAdmin)