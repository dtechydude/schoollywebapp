from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('author', 'date_posted', 'title')

admin.site.register(Post, PostAdmin)
