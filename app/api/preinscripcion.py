# Endpoints de preinscripción
from fastapi import APIRouter

router = APIRouter(prefix="/preinscripcion", tags=["preinscripcion"])

@router.get("/")
def ver_preinscripciones():
    return []

@router.post("/")
def preinscribir():
    return {"message": "Preinscripción realizada"}
