from django import forms
from.models import Notification



class MailForm(forms.ModelForm):
   
    class Meta:
        
        model = Notification
        fields = ('recipient', 'subject', 'content')


# class ReplyMailForm(forms.ModelForm):
#     class Meta:
#         model = ReplyMailForm
#         fields = ('reply_body',)

#         widgets = {
#             'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),