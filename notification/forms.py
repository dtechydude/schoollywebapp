from django import forms
from.models import Notification



class MailForm(forms.ModelForm):
   
    class Meta:
        
        model = Notification
        fields = ('recipient', 'subject', 'content')