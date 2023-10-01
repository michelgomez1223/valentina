from app import db

"""================================================
============== ENTIDADES DEL PROYECTO =============
==================================================="""

class Estudiante(db.Model):
    __tablename__ = "estudiantes"
    numero_documento = db.Column(db.Integer, primary_key = True, unique = True)
    password = db.Column(db.String(255))
    nombre_estudiante = db.Column(db.String(100))
    apellido_estudiante = db.Column(db.String(100))
    tipo_documento = db.Column(db.String(100))
    curso = db.Column(db.Integer)

class Directivo(db.Model):
    __tablename__ = "directivos"
    numero_documento = db.Column(db.Integer, primary_key = True, unique = True)
    password = db.Column(db.String(255))
    nombre_directivo = db.Column(db.String(100))
    apellido_directivo = db.Column(db.String(100))
    tipo_documento = db.Column(db.String(100))
    cargo = db.Column(db.String(100))

class Servicio(db.Model):
    __tablename__ = "servicios"
    id_servicio = db.Column(db.Integer, primary_key = True, unique = True)
    cargo = db.Column(db.String(255))
    descripcion = db.Column(db.String(500))
    cantidad_horas = db.Column(db.Integer)

class Registro(db.Model):
    __tablename__ = "registros"
    id_registro = db.Column(db.Integer, primary_key = True, unique = True)
    dia = db.Column(db.Date)
    hora_inicio = db.Column(db.Time(0))
    hora_fin = db.Column(db.Time(0))
    hora_completadas = db.Column(db.Integer)
    horas_faltantes = db.Column(db.Integer)
    firma= db.Column(db.String(100))
    

