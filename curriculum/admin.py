from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from curriculum.models import Lesson, Standard, Subject

# Register your models here.
class StandardAdmin(admin.ModelAdmin):
   
    list_display=('name', 'description')

class SubjectAdmin(admin.ModelAdmin):
       
    list_display=('subject_id', 'name', 'standard')

class LessonAdmin(admin.ModelAdmin):
       
    list_display=('lesson_id', 'standard', 'subject')
    

admin.site.register(Standard, StandardAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Lesson, LessonAdmin)





class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

