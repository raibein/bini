from django.conf.urls import url
from django.contrib import admin

from .views import (
	contact_list
)


urlpatterns = [
    url(r'^$', contact_list), #eg : url(r'^profiles/$', "<app_name>.views.<function_name>"),
]