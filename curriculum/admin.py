from django.contrib import admin

from curriculum.models import Lesson, Standard, Subject

# Register your models here.

admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Lesson)
