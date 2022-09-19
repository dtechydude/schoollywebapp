from django.urls import path
from . import views
from notification import views as notification_views
from .views import NotificationListView, NotificationDetailView



app_name = 'notification'

urlpatterns = [
    path('', views.NotificationListView.as_view(), name="mail-list"),
    path('self-mail/', notification_views.view_self_notification, name="mail-self"),
    path('self-mail/<int:pk>/', NotificationDetailView.as_view(), name='mail-detail'),
    

    
      
   
]
