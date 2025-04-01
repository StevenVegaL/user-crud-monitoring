from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de conexión para la base de datos PostgreSQL
DATABASE_URL = "postgresql://user:password@postgres:5432/mydb"

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crear una sesión local para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
