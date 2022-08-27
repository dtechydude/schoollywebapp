from django.urls import path
from portal import views as portal_views 


app_name = 'portal'

urlpatterns = [
    path('home/', portal_views.portal_home, name="portal-home"),
    path('studentlist/', portal_views.student_list, name="student-list"),
    path('stafflist/', portal_views.staff_list, name="staff-list"),
    path('elearning/', portal_views.elearning_list, name="elearning-list"),
]
