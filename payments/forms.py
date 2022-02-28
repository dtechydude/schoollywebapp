from django import forms
from payments.models import PaymentDetail


class PaymentForm(forms.ModelForm):
        
        class Meta:
            model = PaymentDetail
            fields = '__all__'
          
