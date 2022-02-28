from django.urls import path
from django.conf.urls.static import static
from staff import views as user_views 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('staff-page/', user_views.staffupdateprofile, name="staff-profile"),
    # path('staff-academic/', user_views.staffacademic, name="staff-academic"),
    path('staff-list/', user_views.stafflist, name="staff-list"),

]