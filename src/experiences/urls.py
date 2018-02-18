from django.conf.urls import url
from django.contrib import admin

from .views import (
	exp_list
)


urlpatterns = [
    url(r'^$', exp_list), #eg : url(r'^profiles/$', "<app_name>.views.<function_name>"),
]