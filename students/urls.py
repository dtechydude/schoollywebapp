from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from students import views as user_views 
from django.contrib.auth import views as auth_views
from students.views import StudentListView

app_name = 'students'

urlpatterns = [
    path('student-page/', user_views.studentpage, name="studentpage"),
    path('student-form/', user_views.studentupdateform, name="studentform"),
    path('student-list/', user_views.studentlist, name="student-list"),
    # path('pdf/<pk>/', user_views.student_render_pdf_view, name="student-pdf-view"),
    path('', StudentListView.as_view(), name="all-students"),    
    path('pdf/<pk>/', user_views.student_render_pdf_view, name="student-pdf-view"),
    path('test-view/', user_views.render_pdf_view, name="test-view"),

    path('student-pdf', user_views.mystudent_pdf, name="student-pdf"),
    path('student-csv', user_views.mystudent_csv, name="student-csv"),
    
 


]