"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

application = get_wsgi_application()
"""

import os
import sys

#path = '/home/pythonanywhereusername/projectname' 
path = '/home/bini/projectname'
if path not in sys.path
	sys.path.append(path)


os.environ['DJANGO_SETTINGS_MODULE'] = 'binita.settings' # binita.settings is the 'projectname.settings'


from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StatisFileHandler
application = StatisFileHandler(get_wsgi_application())

