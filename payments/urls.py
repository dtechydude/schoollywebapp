from django.urls import path
from payments import views as payment_views 

urlpatterns = [
    path('payment-form/', payment_views.payment, name="payment"),
    path('payment-record/', payment_views.paymentlist, name="payment_record"),
    path('my-payments/', payment_views.view_self_payments, name="my_payments"),
    path('make-payment/', payment_views.make_payment, name="make_payment"),
]
