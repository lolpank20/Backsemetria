from app.db.session import engine
from app.models import models

# Crear todas las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print("Tablas creadas correctamente.")
