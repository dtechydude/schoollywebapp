from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PaymentCategory(models.Model):
    name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'{self.name}'


class PaymentChart(models.Model):
    name = models.CharField(max_length=150, blank=True)
    payment_cat = models.ForeignKey(PaymentCategory, on_delete=models.CASCADE)
    amount_due = models.CharField(max_length=150, blank=True)
    
    def __str__ (self):
        return f'{self.name}' 
    

class PaymentDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_name = models.ForeignKey(PaymentChart, on_delete=models.CASCADE)
    amount_paid =models.CharField(max_length=150, blank=False) 
    payment_date = models.DateField()  

    cash = 'cash'
    bank_deposit = 'bank_deposit'
    cheque = 'cheque'
    pos = 'pos'

    payment_methods = [
        (cash, 'cash'),
        (bank_deposit, 'bank_deposit'),
        (cheque, 'cheque'),
        (pos, 'pos'),
    ]
    payment_method = models.CharField(max_length=50, choices=payment_methods, blank=True)  
    depositor = models.CharField(max_length=150, blank=True) 
    bank_name = models.CharField(max_length=150, blank=True) 
    teller = models.CharField(max_length=150, blank=True) 
    description = models.CharField(max_length=200, blank=True)
    confirmed = models.BooleanField(default=False)     


    def __str__ (self):
        return f'{self.user}'
    