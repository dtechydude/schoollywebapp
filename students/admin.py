from django.contrib import admin

from students.models import StudentAcademicInfo, StudentProfile

# Register your models here.
admin.site.register(StudentAcademicInfo)
admin.site.register(StudentProfile)