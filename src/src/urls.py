"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^bini-super/', admin.site.urls),    
    url(r'^', include("profiles.urls", namespace='profiles')),
	#url(r'^profiles/$', "<app_name>.views.<function_name>"),
    url(r'^skills/', include("professional_skills.urls", namespace='professional_skills')),
    url(r'^experiences/', include("experiences.urls", namespace='experiences')),
    url(r'^awards/', include("awards.urls", namespace='awards')),
    url(r'^events/', include("events.urls", namespace='events')),
    url(r'^contact/', include("contacts.urls", namespace='contacts')),
    url(r'^projects/', include("projects.urls", namespace='projects')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    