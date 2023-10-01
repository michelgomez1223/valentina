from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, PasswordField


class RegistrarEstudianteForms(FlaskForm):
    numero_documento = IntegerField("Digita tus nombres")
    password = PasswordField("Digita Tu Contraseña")
    nombre_estudiante = StringField("Digita Tus Nombres")
    apellido_estudiante = StringField("Digita Tus Apellidos")
    tipo_documento = StringField("Digitas Tipo De Documento")
    curso = IntegerField("Digita Tu Curso")
    submit = SubmitField("Registrar Datos")
