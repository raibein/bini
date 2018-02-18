from django.conf.urls import url
from django.contrib import admin

from .views import (
	awards_list
)


urlpatterns = [
    url(r'^$', awards_list), #eg : url(r'^profiles/$', "<app_name>.views.<function_name>"),
]