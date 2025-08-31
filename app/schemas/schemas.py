from pydantic import BaseModel
from typing import Optional, List

class CarreraBase(BaseModel):
    nombre: str

class CarreraCreate(CarreraBase):
    pass

class Carrera(CarreraBase):
    id: int
    class Config:
        orm_mode = True

class HorarioMateriaBase(BaseModel):
    dia: str
    hora_inicio: str
    hora_fin: str
    ciclo: Optional[int]

class HorarioMateriaCreate(HorarioMateriaBase):
    pass

class HorarioMateria(HorarioMateriaBase):
    id: int
    class Config:
        orm_mode = True

class MateriaBase(BaseModel):
    codigo: str
    nombre: str
    creditos: int
    profesor: str
    cupos: int
    ciclo: Optional[int]
    tipo: str
    carrera_id: int

class MateriaCreate(MateriaBase):
    horarios: List[HorarioMateriaCreate]

class Materia(MateriaBase):
    id: int
    horarios: List[HorarioMateria] = []
    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nombre: str
    email: str
    rol: str
    carrera_id: Optional[int]

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True

class PreinscripcionBase(BaseModel):
    materia_id: int
    ciclo: int

class PreinscripcionCreate(PreinscripcionBase):
    pass

class Preinscripcion(PreinscripcionBase):
    id: int
    estudiante_id: int
    estado: str
    class Config:
        orm_mode = True
