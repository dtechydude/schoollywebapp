from django.urls import path
from payment import views as payment_views

app_name = 'payment'

urlpatterns = [
    path('payment-form/', payment_views.payment, name="payment_form"),
    path('payment-record/', payment_views.paymentlist, name="payment_record"),
    path('my-payments/', payment_views.view_self_payments, name="my_payments"),
    path('make-payment/', payment_views.make_payments, name="make_payment"),
    path('payment-pdf', payment_views.mypayment_pdf, name="payment-pdf"),
    path('payment-csv', payment_views.mypayment_csv, name="payment-csv"),
]
