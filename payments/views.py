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



@login_required
def view_self_payments(request):
    mypayment = PaymentDetail.objects.filter(user=request.user)
    context = {
        'mypayment':mypayment
    }
    
    return render(request, 'payments/view_self_payment.html', context)

# FUNCTION FOR DOWNLOADING FILE
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/file")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404




def make_payment(request):
    return render(request, 'payments/make_payment.html')



