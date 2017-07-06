import os
import sys
import site
from django.core.wsgi import get_wsgi_application  # isort:skip

site.addsitedir('/home/nkannielai/webapps/django/panda/panda-env/lib/python3.6/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

activate_this = os.path.expanduser("/home/nkannielai/webapps/django/panda/panda-env/bin/activate_this.py")
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Calculate the path based on the location of the WSGI script
project = '/home/nkannielai/webapps/django/panda/panda/'
workspace = os.path.dirname(project)
sys.path.append(workspace)

sys.path = ['/home/nkannielai/webapps/django/panda/panda', ] + sys.path

application = get_wsgi_application()
