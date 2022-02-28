from django.urls import path
from payments import views as payment_views 

urlpatterns = [
    path('payment-form/', payment_views.payment, name="payment"),
    path('payment-record/', payment_views.paymentlist, name="payment-record"),
]
