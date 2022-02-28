from django.contrib import admin

from payments.models import FeesPayments, PaymentDetail

# Register your models here.
admin.site.register(PaymentDetail)
admin.site.register(FeesPayments)