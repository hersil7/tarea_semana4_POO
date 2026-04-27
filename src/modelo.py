# Clases base del sistema académico según el UML

class Facultad:
    def __init__(self, nombre, codigo, direccion):
        self.nombre = nombre
        self.codigo = codigo
        self.direccion = direccion
        self.carreras = []

class Carrera:
    def __init__(self, nombre, codigo, duracion, anio_acreditacion, facultad):
        self.nombre = nombre
        self.codigo = codigo
        self.duracion = duracion
        self.anio_acreditacion = anio_acreditacion
        self.facultad = facultad
        self.asignaturas = []

class Asignatura:
    def __init__(self, nombre, codigo, creditos, tipo):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.tipo = tipo
        self.cursos = []

class Curso:
    def __init__(self, semestre, horario, modalidad, asignatura):
        self.semestre = semestre
        self.horario = horario
        self.modalidad = modalidad
        self.asignatura = asignatura
        self.estudiantes = []
        self.docente = None

class Persona:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut

class Estudiante(Persona):
    def __init__(self, nombre, rut, matricula, beca, metodo_pago):
        super().__init__(nombre, rut)
        self.matricula = matricula
        self.beca = beca
        self.metodo_pago = metodo_pago
        self.cursos = []

class Docente(Persona):
    def __init__(self, nombre, rut, especialidad, tipo_contrato):
        super().__init__(nombre, rut)
        self.especialidad = especialidad
        self.tipo_contrato = tipo_contrato
        self.cursos = []
