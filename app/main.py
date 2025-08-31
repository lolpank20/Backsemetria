# Punto de entrada principal de FastAPI
from fastapi import FastAPI
from app.api import auth, materias, preinscripcion, admin

app = FastAPI()

# Incluir routers
app.include_router(auth.router)
app.include_router(materias.router)
app.include_router(preinscripcion.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "API de Inscripción de Materias"}
