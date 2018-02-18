from django.conf.urls import url
from django.contrib import admin

#from . import views as pro_view

from .views import (
	pro_list,
	pro_create,
	pro_update,
	pro_delete,
	pro_detail
)


urlpatterns = [
    url(r'^$', pro_list), #url(r'^pros/$', "<app_name>.views.<function_name>"),
    url(r'^create/$', pro_create),
    url(r'^(?P<id>\d+)/edit/$', pro_update),
    url(r'^(?P<id>\d+)/delete/$', pro_delete),
    url(r'^(?P<id>\d+)/$', pro_detail, name='detail'),
]