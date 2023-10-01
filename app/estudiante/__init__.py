from flask import Blueprint 

estudiante = Blueprint('estudiante',
                       __name__,
                       url_prefix = "/estudiante",
                       template_folder = 'templates')

from . import routes