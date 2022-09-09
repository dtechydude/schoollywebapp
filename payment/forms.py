from django import forms
from payment.models import PaymentDetail


class PaymentForm(forms.ModelForm):
        
        class Meta:
            model = PaymentDetail
            fields = ['payment_name', 'payment_date',
                        'payment_method', 'amount_paid',
                        'depositor', 'bank_name', 'teller', 'description']
                        #Note that i removed user because it is an instance in the view already
          
