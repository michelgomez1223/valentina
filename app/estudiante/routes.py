from flask import render_template
from app.estudiante import estudiante
from app import db
from werkzeug.security import generate_password_hash
from app.models import Estudiante
from .forms import RegistrarEstudianteForms

@estudiante.route('/registrar' , methods=['GET','POST'])
def registrarEstudiante():  
    form = RegistrarEstudianteForms()
    if form.validate_on_submit():
        datos_estudiante = Estudiante(
            numero_documento = form.numero_documento.data,
            password = generate_password_hash(form.password.data),
            nombre_estudiante = form.nombre_estudiante.data,
            apellido_estudiante = form.apellido_estudiante.data,
            tipo_documento = form.tipo_documento.data,
            curso = form.curso.data,
        )
        db.session.add(datos_estudiante)
        db.session.commit()
    return render_template('registrar.html', form = form)
    
