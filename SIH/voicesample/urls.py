from django.conf.urls import url
from . import views
from .views import *	
app_name = 'voicesample'

urlpatterns = [
 	url(r'^$', views.index, name='index'),
    ]


