from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from students import views as user_views 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('student-page/', user_views.studentpage, name="studentpage"),
    path('student-profile/', user_views.studentupdateprofile, name="student_profile"),
    path('student-list/', user_views.studentlist, name="student-list"),

]