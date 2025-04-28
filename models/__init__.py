from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# 💡 Definir primero `engine`, `Base` y `session` antes de importar modelos
DATABASE_URL = "postgresql+psycopg2://postgres:5432@localhost:5432/factura_sem_2_123"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

# 💡 Ahora importar modelos
from .usuarios import Usuarios  # ✅ Debe ir después de definir `Base`


"""

from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
 





engine = create_engine("postgresql+psycopg2://postgres:5432@localhost:5432/factura_sem_2_123")

connection = engine.connect()

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)

session = Session()

"""