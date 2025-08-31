# Endpoints de materias
from fastapi import APIRouter

router = APIRouter(prefix="/materias", tags=["materias"])

@router.get("/")
def listar_materias():
    return []

@router.get("/{id}")
def detalle_materia(id: int):
    return {"id": id}
