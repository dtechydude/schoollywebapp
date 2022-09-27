from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve






urlpatterns = [
    path('admin/', admin.site.urls),
    path('curriculum/', include('curriculum.urls')),
    path('', include('pages.urls')),
    path('payment/', include('payment.urls')),
    path('users/', include('users.urls')),
   
    path('results/', include('results.urls', namespace='results')),
    path('students/', include('students.urls', namespace='students')),
    path('staff/', include('staff.urls')),

    path('attendance/', include('attendance.urls')),
    path('demoschool', include('demoschool.urls')),
    path('portal/', include('portal.urls')),
    path('quizes/', include('quizes.urls', namespace = 'quizes')),
    path('blog/', include('blog.urls', namespace = 'blog')),
    path('notification/', include('notification.urls', namespace = 'notification')),
    # path('demoschool/', include('demoschool.urls')),

    # path('ckeditor', include('ckeditor_uploader.urls')),    #for ckeditor image upload

    

#PATH FOR DOWNLOAD URL
   url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),

  


    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)