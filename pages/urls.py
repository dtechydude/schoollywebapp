
from django.urls import path
from pages import views as page_views


urlpatterns = [

    path('', page_views.homepage, name='home'),
    path('contact/', page_views.contact, name='contact'),
    # path('pages/', include('pages.urls')),
    
]
