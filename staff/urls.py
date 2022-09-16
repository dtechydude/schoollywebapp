from django.urls import path
from django.conf.urls.static import static
from staff import views as user_views 
from django.contrib.auth import views as auth_views
from .views import StaffDetailView

app_name = 'staff'

urlpatterns = [
    path('staffform/', user_views.staffupdateprofile, name="staff_form"),
    # path('staff-academic/', user_views.staffacademic, name="staff-academic"),
    path('stafflist/', user_views.stafflist, name="staff_list"),
    path('staffform/<str:id>/', StaffDetailView.as_view(), name="staff_detail"),
    path('staff-pdf', user_views.staff_pdf, name="staff-pdf"),
    path('staff-csv', user_views.staff_csv, name="staff-csv"),

]