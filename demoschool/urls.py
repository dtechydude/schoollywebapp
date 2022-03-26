from django.urls import path
from demoschool import views as user_views 



app_name = 'school'

urlpatterns = [
    path('', user_views.demoschool, name="demoschool"),
    path('allcourses/', user_views.allcourses, name="all_courses"),
    path('gallery/', user_views.school_gallery, name="school_gallery"),
    path('test/', user_views.test, name="test"),


]