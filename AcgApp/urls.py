from django.conf.urls import include, url
from . import views
from django.contrib import admin
# from .views import contact,imbuto,imishwi,ifumbire,contact_us

urlpatterns = [
    url(r'^imbuto', views.imbuto, name='imbuto'),
    url(r'^imishwi', views.imishwi, name='imishwi'),
    url(r'^ifumbire', views.ifumbire, name='ifumbire'),
    url(r'^contact',views.contact, name='contact'),
    url(r'^contact_us', views.contact_us, name='contact_us')
      
]