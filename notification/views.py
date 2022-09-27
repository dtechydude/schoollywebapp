from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, DeleteView, CreateView
from django.http import Http404, HttpResponseRedirect, HttpResponse
from notification.models import Notification
from .forms import MailForm
from django.contrib.auth.models import User
import os



class NotificationListView(ListView):
    model = Notification
    template_name = 'notification/mail_list.html'
    context_object_name = 'notification'


class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notification/mail_detail.html'
    context_object_name = 'mails'


class NotificationCreateView(CreateView):
    form_class = MailForm
    context_object_name = 'notification'
    model = Notification
    template_name = 'notification/send_mail.html'

    def form_valid(self, form, *args, **kwargs):
        form.instance.sender = self.request.user
        return super().form_valid(form)



class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notification/notification_detail.html'


@login_required
def view_self_notification(request, **kwargs):
# this issue was solved by me.
    try:     
        mymail = Notification.objects.filter(recipient=User.objects.get(username=request.user))
    
        context = {
            'mymail':mymail
            
        }    
    
        return render(request, 'notification/view_self_mail.html', context)

    except Notification.DoesNotExist:
        return HttpResponse('You are not a registered')
        

# FUNCTION FOR DOWNLOADING FILE
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/file")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404





