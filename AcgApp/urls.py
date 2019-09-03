from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^imbuto', views.imbuto, name='imbuto'),
    url(r'^imishwi', views.imishwi, name='imishwi'),
    url(r'^ifumbire', views.ifumbire, name='ifumbire'),
    url(r'^contact',views.contact, name='contact'),
      
]