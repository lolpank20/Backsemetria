# Backsemetria - Backend FastAPI

Este proyecto es el backend de la plataforma de inscripción de materias, desarrollado con FastAPI, SQLAlchemy y SQLite.

## Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/lolpank20/Backsemetria.git
   cd Backsemetria
   ```

2. **(Opcional) Crea un entorno virtual:**
   ```bash
   python -m venv venv
   # Activa el entorno virtual:
   # En Windows:
   venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   python -m pip install --upgrade pip
   python -m pip install fastapi uvicorn sqlalchemy pandas openpyxl
   ```

4. **Inicializa la base de datos:**
   ```bash
   python app/db/init_db.py
   ```

5. **Inicia el servidor FastAPI:**
   ```bash
   python -m uvicorn app.main:app --reload
   ```

6. **Accede a la documentación interactiva:**
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints principales
- `/auth/*` : Autenticación y registro de usuarios
- `/materias/*` : Consulta de materias
- `/preinscripcion/*` : Preinscripción de materias
- `/admin/cargar_excel` : Carga masiva de materias desde archivo Excel

## Carga de datos desde Excel
El endpoint `/admin/cargar_excel` espera un archivo Excel con las siguientes columnas:
- `codigo`
- `nombre`
- `creditos`
- `profesor`
- `cupos`
- `ciclo`
- `tipo`
- `carrera_id`

## Notas
- El archivo de base de datos SQLite se crea automáticamente como `app.db` en la raíz del proyecto.
- Puedes modificar los modelos y endpoints según las necesidades de tu institución.

## Licencia
MIT
