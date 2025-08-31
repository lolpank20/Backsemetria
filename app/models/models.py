from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base

class Carrera(Base):
    __tablename__ = "carreras"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    materias = relationship("Materia", back_populates="carrera")

class Materia(Base):
    __tablename__ = "materias"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True)
    nombre = Column(String, index=True)
    creditos = Column(Integer)
    profesor = Column(String)
    cupos = Column(Integer)
    ciclo = Column(Integer)  # 1, 2 o None para semestre completo
    tipo = Column(String)    # obligatoria, electiva, transversal
    carrera_id = Column(Integer, ForeignKey("carreras.id"))
    carrera = relationship("Carrera", back_populates="materias")
    horarios = relationship("HorarioMateria", back_populates="materia")

class HorarioMateria(Base):
    __tablename__ = "horarios_materia"
    id = Column(Integer, primary_key=True, index=True)
    materia_id = Column(Integer, ForeignKey("materias.id"))
    dia = Column(String)  # Ej: 'Lunes', 'Martes', etc.
    hora_inicio = Column(String)  # '08:00'
    hora_fin = Column(String)     # '10:00'
    ciclo = Column(Integer)       # 1, 2 o None
    materia = relationship("Materia", back_populates="horarios")

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    rol = Column(String)  # estudiante, admin
    carrera_id = Column(Integer, ForeignKey("carreras.id"), nullable=True)
    carrera = relationship("Carrera")

class Preinscripcion(Base):
    __tablename__ = "preinscripciones"
    id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(Integer, ForeignKey("usuarios.id"))
    materia_id = Column(Integer, ForeignKey("materias.id"))
    estado = Column(String, default="pendiente")  # pendiente, confirmada
    ciclo = Column(Integer)
    estudiante = relationship("Usuario")
    materia = relationship("Materia")
