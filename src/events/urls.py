from django.conf.urls import url
from django.contrib import admin

from .views import (
	events_list
)


urlpatterns = [
    url(r'^$', events_list), #eg : url(r'^profiles/$', "<app_name>.views.<function_name>"),
]