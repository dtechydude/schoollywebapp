from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ManyToManyField(User, related_name='send_mail')
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    attachement = models.CharField(max_length=1000)
    date_sent = models.DateTimeField()

    def __str__(self):
        return f'{self.sender}'

    def get_absolute_url(self):
        return reverse('notification:notice-detail', kwargs={'id':self.id})


class MailReply(models.Model):
    notification_name = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='replies')
    reply_body = models.TextField(max_length=500)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to" + str(self.sender.sender)

