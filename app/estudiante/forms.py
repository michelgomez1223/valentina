from flask_wtf import Flaskform
from wtform import SubmitField, IntegerField, StringField


class RegistrarEstudianteForms(Flaskform):
    numero_documento = IntegerField("Digita tus nombres")
    password = StringField("Digita Tu Contraseña")
    nombre_estudiante = StringField("Digita Tus Nombres")
    apellido_estudiante = StringField("Digita Tus Apellidos")
    tipo_documento = StringField("Digitas Tipo De Documento")
    curso = IntegerField("Digita Tu Curso")
    submit = SubmitField("Registrar Datos")
