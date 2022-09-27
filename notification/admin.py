from django.contrib import admin
from .models import Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display=('sender', 'date_sent', 'subject')


admin.site.register(Notification, NotificationAdmin)
