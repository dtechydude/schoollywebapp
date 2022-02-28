from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def homepage(request):
    return render(request, 'pages/index.html')




def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['support@gmail.com'] #to email
            ,
            )
   
        return render(request, 'pages/contact.html', {'message_name': message_name})
    else:
        return render(request, 'pages/contact.html')
