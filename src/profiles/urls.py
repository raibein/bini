from django.conf.urls import url
from django.contrib import admin

#from . import views as profile_view

from .views import (
	profile_list,	
	#proff_list,
	profile_create,
	profile_update,
	profile_delete,
	profile_detail
)


urlpatterns = [
    url(r'^$', profile_list), #url(r'^profiles/$', "<app_name>.views.<function_name>"),    
    #url(r'^$', proff_list),
    url(r'^create/$', profile_create),
    url(r'^(?P<id>\d+)/edit/$', profile_update),
    url(r'^(?P<id>\d+)/delete/$', profile_delete),
    url(r'^(?P<id>\d+)/$', profile_detail, name='detail'),
]