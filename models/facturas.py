from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
from src.models.clientes import Clientes
from src.models.usuarios import Usuarios

class Facturas(Base):
    __tablename__ = "facturas"    
    id = Column(Integer, primary_key=True)
    numero_factura = Column(String(20), unique=True, nullable=False)
    fecha_factura = Column(String(20), nullable=False)
    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    def __init__(self, numero_factura, fecha_factura, id_cliente, id_usuario):
        self.numero_factura = numero_factura
        self.fecha_factura = fecha_factura
        self.id_cliente = id_cliente
        self.id_usuario = id_usuario

    
    def obtener_facturas():
        facturas = (session.query(Facturas, Clientes, Usuarios)
                           .join(Clientes, Facturas.id_cliente == Clientes.id)
                           .join(Usuarios, Facturas.id_usuario == Usuarios.id)).all()
        return facturas 
    
    def agregar_factura(factura):
        factura = session.add(factura)
        session.commit()
        return factura    
    
    