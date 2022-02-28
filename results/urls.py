from django.urls import path

from django.conf.urls.static import static
from results import views as result_views 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('print-result/', result_views.printresult, name="print-result"),
    path('upload-result/', result_views.uploadresult, name="upload_result"),
      
   
]
