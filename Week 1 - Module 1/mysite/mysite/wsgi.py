import os
import sys

path = os.path.expanduser('~/django_projects/mysite')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())


# import os
# import sys

# # assuming your django settings file is at '/home/Phani/mysite/mysite/settings.py'
# # and your manage.py is is at '/home/Phani/mysite/manage.py'
# path = '/home/Phani/django_projects/mysite/mysite/'
# if path not in sys.path:
#     sys.path.append(path)
#     # sys.path.insert(0, path)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# # then:
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()