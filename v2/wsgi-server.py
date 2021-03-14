from waitress import serve
from help_the_helpless.wsgi import application

serve(application, port="80")
