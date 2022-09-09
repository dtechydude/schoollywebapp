from django.contrib import admin
from payment.models import PaymentCategory, PaymentChart, PaymentDetail

# Register your models here.
class PaymentCategoryAdmin(admin.ModelAdmin):
    list_display=('name',)

class PaymentChartAdmin(admin.ModelAdmin):
    
    list_display=('name', 'payment_cat', 'amount_due')

class PaymentDetailAdmin(admin.ModelAdmin):
    
    list_display=('user', 'payment_name', 'amount_paid', 'payment_date')
    


admin.site.register(PaymentCategory)
admin.site.register(PaymentChart)
admin.site.register(PaymentDetail)
