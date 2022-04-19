from django.shortcuts import render, redirect
from payments.forms import PaymentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from payments.models import PaymentDetail
from django.http import HttpResponse
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# for csv
import csv



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



# Funtion for payment
def make_payment(request):
    return render(request, 'payments/make_payment.html')

#  Function for pdf and csv



# Generate a PDF staff list
def mypayment_pdf(request):
    # create Bytestream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 12)
    # Add some lines of text
    # lines = [
    #     "This is line 1",
    #     "This is line 2",
    #     "This is line31",
    #     "This is line 4",
    # ]
    # Designate the model
    payment = PaymentDetail.objects.all()

    # Create a blank list
        
    lines = [" PAYMENT DETAIL REPORT"]

    for payments in payment:
        lines.append(""),
        lines.append("Username: " + payments.user.username),
        lines.append("Amount: " + str(payments.amount_paid)),
        lines.append("Date: " + str(payments.payment_date)),
        lines.append("Method:" + payments.payment_method),
       
        lines.append("------->----------->----------->"),


    # loop
    for line in lines:
        textob.textLine(line)
    #fininsh up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    # Return something
    return FileResponse(buf, as_attachment=False, filename='payment.pdf')


# Generate a CSV staff list
def mypayment_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename=payment.csv'
    
# Create a csv writer
    writer = csv.writer(response)

    payment = PaymentDetail.objects.all()
    
    # Add column headings to the csv files
    writer.writerow(['Username ', 'Amount', 'Date', 'Method'])


    # Loop thru and output
    for payments in payment:
        writer.writerow([payments.user.username, payments.amount_paid, payments.payment_date, payments.payment_method])
        
    return response



