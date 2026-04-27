# Script de prueba para el sistema académico
from modelo import Facultad, Carrera, Asignatura, Curso, Estudiante, Docente

# Crear una facultad
facultad = Facultad("Facultad de Ingeniería", "FI01", "Av. Universidad 123")

# Crear una carrera y asociarla a la facultad
carrera = Carrera("Ingeniería Informática", "INF01", 5, 2025, facultad)
facultad.carreras.append(carrera)

# Crear una asignatura y asociarla a la carrera
asignatura = Asignatura("Programación Orientada a Objetos", "POO01", 6, "Obligatoria")
carrera.asignaturas.append(asignatura)

# Crear un curso y asociarlo a la asignatura
curso = Curso("2026-1", "Lun 10-12", "Presencial", asignatura)
asignatura.cursos.append(curso)

# Crear un docente y asignarlo al curso
docente = Docente("Dra. Ana Pérez", "12.345.678-9", "Software", "Planta")
curso.docente = docente
docente.cursos.append(curso)

# Crear un estudiante y matricularlo en el curso
estudiante = Estudiante("Juan Soto", "21.987.654-3", "20261234", "Beca Mérito", "Contado")
curso.estudiantes.append(estudiante)
estudiante.cursos.append(curso)

# Mostrar información básica
print(f"Facultad: {facultad.nombre}, Carreras: {[c.nombre for c in facultad.carreras]}")
print(f"Carrera: {carrera.nombre}, Asignaturas: {[a.nombre for a in carrera.asignaturas]}")
print(f"Asignatura: {asignatura.nombre}, Cursos: {[c.semestre for c in asignatura.cursos]}")
print(f"Curso: {curso.semestre}, Docente: {curso.docente.nombre}, Estudiantes: {[e.nombre for e in curso.estudiantes]}")
