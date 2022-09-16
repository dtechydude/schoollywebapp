from django.contrib import admin

from staff.models import Department, StaffCategory, StaffProfile

# Register your models here.

admin.site.register(StaffCategory)
admin.site.register(StaffProfile)
# admin.site.register(StaffAcademicInfo)
admin.site.register(Department)
