from flask import Flask
from .config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .general import index

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)

#inicializar a continuacion el objeto SQLalchemy 
db=SQLAlchemy(app)
Migrate(app , db)

from app.estudiante import estudiante


#importar desde aqui para evitar errores con db

app.register_blueprint(index)
app.register_blueprint(estudiante)





from .models import Estudiante,Directivo,Registro,Servicio