from django.conf.urls import url
from django.contrib import admin

from .views import (
	projects_list,
	gallery_list,
)


urlpatterns = [
    url(r'^$', projects_list), #eg : url(r'^profiles/$', "<app_name>.views.<function_name>"),
    url(r'(?P<id>\d+)/galleries/$', gallery_list, name='galleries'), #url(r'^profiles/$', "<app_name>.views.<function_name>"),
]