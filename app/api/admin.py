# Endpoints administrativos
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
from app.db.session import SessionLocal
from app.models.models import Materia

router = APIRouter(prefix="/admin", tags=["admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/materias")
def crear_materia():
    return {"message": "Materia creada"}

@router.post("/datos/prueba")
def generar_datos_prueba():
    return {"message": "Datos de prueba generados"}

# Nuevo endpoint para cargar datos desde Excel
@router.post("/cargar_excel")
async def cargar_excel(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        df = pd.read_excel(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error leyendo el archivo: {str(e)}")
    count = 0
    for _, row in df.iterrows():
        materia = Materia(
            codigo=row['codigo'],
            nombre=row['nombre'],
            creditos=row['creditos'],
            profesor=row['profesor'],
            cupos=row['cupos'],
            ciclo=row.get('ciclo'),
            tipo=row['tipo'],
            carrera_id=row['carrera_id']
        )
        db.add(materia)
        count += 1
    db.commit()
    return {"message": f"{count} materias cargadas correctamente"}
