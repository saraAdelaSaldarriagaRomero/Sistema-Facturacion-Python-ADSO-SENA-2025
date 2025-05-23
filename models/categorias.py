from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Categorias(Base):
    __tablename__ = "categorias"    
    id = Column(Integer, primary_key=True)
    categoria = Column(String(300), unique=True, nullable=False)

    def __init__(self, categoria):
        self.categoria = categoria
    
    def obtener_categorias():
        categorias = session.query(Categorias).all()
        return categorias 
