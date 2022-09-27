from doctest import Example
from django.contrib import admin

from results.models import Examination, PrintResult, Result, Session

# Register your models here.

class PrintResultAdmin(admin.ModelAdmin):
       
    list_display=('student', 'exam', 'session')


admin.site.register(Result)
admin.site.register(Examination)
admin.site.register(Session)
admin.site.register(PrintResult, PrintResultAdmin)
