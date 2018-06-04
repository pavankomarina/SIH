from django.conf.urls import url
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'voice'

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^upload/$',views.simple_upload,name='upload'),
    url(r'^record/$',views.record,name='record'),
    url(r'^comparision/$',views.comparevoice,name='comparision'),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
