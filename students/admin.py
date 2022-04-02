from django.contrib import admin

from students.models import Mystudents, StudentDetail, StudentProfile

# Register your models here.
admin.site.register(StudentDetail)
admin.site.register(StudentProfile)
# admin.site.register(Mystudents)