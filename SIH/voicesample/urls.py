from django.conf.urls import url
from . import views
from .views import *
app_name = 'voicesample'

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    ]


