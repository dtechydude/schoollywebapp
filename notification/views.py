from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, DeleteView, CreateView
 
from notification.models import Notification
from .forms import MailForm



class NotificationListView(ListView):
    model = Notification
    template_name = 'notification/mail_list.html'


class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notification/mail_detail.html'


class NotificationCreateView(CreateView):
    form_class = MailForm
    context_object_name = 'notification'
    model = Notification
    template_name = 'notification/mail_create.html'
    
    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.sender = self.request.user
        fm.recipient = self.object.recipient
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notification/notification_detail.html'







