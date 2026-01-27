import os
from mangum import Mangum
from friendsofscoiety.asgi import application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "friendsofsociety.settings")
handler = Mangum(application)
