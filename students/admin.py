from django.contrib import admin

from students.models import Mystudents, StudentDetail, StudentProfile

class StudentAdmin(admin.ModelAdmin):
       
    list_display=('user', 'current_class', 'date_admitted', 'parent_phone')

# Register your models here.
admin.site.register(StudentDetail, StudentAdmin)
admin.site.register(StudentProfile)
# admin.site.register(Mystudents)