from django.contrib import admin

from users.models import Profile

class UserProfileAdmin(admin.ModelAdmin):
       
    list_display=('user', 'code', 'gender', 'user_type')

# Register your models here.
admin.site.register(Profile, UserProfileAdmin)
