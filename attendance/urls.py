from django.urls import path
from attendance import views as attendance_views


urlpatterns = [

    
    path('attendance-form/', attendance_views.attendance_form, name='attendance_form'),
    path('attendance-view/', attendance_views.attendance_view, name='attendance_view'),
 
    
]
