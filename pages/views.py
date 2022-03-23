from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request, 'pages/index.html')




def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']
        messages.success(request, f'New user account has been created. You can register another user.')


        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['support@gmail.com'] #to email
            ,
            )
   
        return render(request, 'pages/contact.html', {'message_name': message_name})
    else:
        return render(request, 'pages/contact.html', {'title': 'Contact Us'})


def affiliate(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']
        messages.success(request, f'New user account has been created. You can register another user.')


        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['support@gmail.com'] #to email
            ,
            )
   
        return render(request, 'pages/affiliate.html', {'message_name': message_name})
    else:
        return render(request, 'pages/affiliate.html', {'title': 'Affiliate'})


def demo(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']
        messages.success(request, f'New user account has been created. You can register another user.')


        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['support@gmail.com'] #to email
            ,
            )
   
        return render(request, 'pages/demo.html', {'message_name': message_name})
    else:
        return render(request, 'pages/demo.html', {'title': 'Demo'})


