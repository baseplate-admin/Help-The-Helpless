from waitress import serve
from djangoProject.wsgi import application

serve(application, port='8000')