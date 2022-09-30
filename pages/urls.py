
from django.urls import path
from pages import views as page_views

app_name ='pages'

urlpatterns = [

    path('demoschool/', page_views.homepage, name='home'),
    path('', page_views.schoolly_home, name='schoolly_home'),
    path('contact/', page_views.contact, name='contact'),
    path('affiliate/', page_views.affiliate, name='affiliate'),
    path('demo/', page_views.demo, name='demo'),
    # path('pages/', include('pages.urls')),
    
]
