from django.urls import path
from portal import views as portal_views 


app_name = 'portal'

urlpatterns = [
    path('home/', portal_views.portal_home, name="portal-home"),

]
