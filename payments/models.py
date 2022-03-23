from django.db import models
from django.contrib.auth.models import User


class FeesPayments(models.Model):
    name = models.CharField(max_length=150, blank=True)
    category = models.CharField(max_length=150, blank=True)  #test, exam, quiz
    
    def __str__ (self):
        return f'{self.name} Fees'

class PaymentDetail(models.Model):
    # student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    payment_name = models.ForeignKey(FeesPayments, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)
    amount_due = models.CharField(max_length=150, blank=True) 
    amount_paid =models.CharField(max_length=150, blank=True) 
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
    balance_due =  models.CharField(max_length=150, blank=True) 
    


    def __str__ (self):
        return f'{self.user.username} - {self.payment_date}' 
    
 
    

  
    