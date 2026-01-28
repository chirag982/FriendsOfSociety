import os
from mangum import Mangumfrom 
from friendsofscoiety.asgi import application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "friendsofsociety.settings")