from django.shortcuts import render, redirect

from payments.forms import PaymentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from payments.models import PaymentDetail

# Create your views here.
@login_required
def payment(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment_form.save()
          
            messages.success(request, f'The Payment has been entered successfully')
            return redirect('payment')
    else:
        payment_form = PaymentForm()
    
    context ={
        'payment_form' : payment_form
    }
    return render(request, 'payments/payment_form.html', context)


@login_required
def paymentlist(request):
    # model = PaymentDetail
    # template_name = 'payments/payment_list.html'
    # context_objects_name = 'paymentlist'
    # ordering = ['-payment_date']

    context = {
        'paymentlist' : PaymentDetail.objects.all()

    }
    return render (request, 'payments/payment_list.html', context )
