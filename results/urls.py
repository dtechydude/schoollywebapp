from django.urls import path

from django.conf.urls.static import static
from results import views as result_views 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('print-result/', result_views.printresult, name="print-result"),
    path('print-resultform/', result_views.printresultform, name="print-resultform"),
    path('upload-result/', result_views.uploadresult, name="upload-result"),
    path('my-result/', result_views.view_self_result, name="my-result"),
      
   
]
