from django.urls import path
from demoschool import views as user_views 



app_name = 'demoschool'

urlpatterns = [
    path('', user_views.demoschool, name="demoschool"),
    path('allcourses/', user_views.allcourses, name="all_courses"),
    path('gallery/', user_views.school_gallery, name="school_gallery"),
    path('test/', user_views.test, name="test"),
    path('contact/', user_views.contact_us, name="contact_us"),
    path('about/', user_views.about_us, name="about_us"),
    path('admission/', user_views.admission, name="admission"),
    path('gallery/', user_views.school_gallery, name="school_gallery"),


]