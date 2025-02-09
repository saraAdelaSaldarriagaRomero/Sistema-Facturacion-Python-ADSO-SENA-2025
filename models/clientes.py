from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from src.models import session, Base

class Clientes(Base, SerializerMixin):
    __tablename__ = "clientes"    
    id = Column(Integer, primary_key=True)
    numero_identificacion = Column(String(30), unique=True, nullable=False)
    nombre_completo = Column(String(200), nullable=False)
    direccion = Column(String(300), nullable=False)
    telefono = Column(String(30), nullable=False)
    email = Column(String(500), unique=True, nullable=False)

    def __init__(self, 
                 numero_identificacion, 
                 nombre_completo, 
                 direccion, telefono, 
                 email):
        self.numero_identificacion = numero_identificacion
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
    
    def obtener_clientes():
        clientes = session.query(Clientes).all()
        print(clientes)
        return clientes 
    
    
    
    def agregar_cliente(cliente):
       cliente = session.add(cliente)
       session.commit()
       return cliente 
    
    def eliminar_cliente(id):
        cliente = session.query(Clientes).get(id)        
        session.delete(cliente)
        session.commit()
        return cliente
     
    def actualizar_cliente(cliente, id):
        # Obtener el cliente existente por ID
        cliente_modificar = session.query(Clientes).get(id)
        
        if cliente_modificar:
            # Actualizar los atributos del cliente con los nuevos valores
            cliente_modificar.numero_identificacion = cliente.numero_identificacion
            cliente_modificar.nombre_completo = cliente.nombre_completo
            cliente_modificar.direccion = cliente.direccion
            cliente_modificar.telefono = cliente.telefono
            cliente_modificar.email = cliente.email

            # Guardar los cambios en la base de datos
            session.commit()
            return cliente_modificar
        else:
            return None
    

    @staticmethod
    def obtener_cliente_por_id(id):
      cliente = session.query(Clientes).get(id)
      return cliente.to_dict()
    

    def obtener_cliente_por_numero_identificacion(numero_identificacion):
        print(numero_identificacion)
        id= int(numero_identificacion)
        cliente = session.query(Clientes).filter(Clientes.numero_identificacion==numero_identificacion).first()
        print(cliente)
        return cliente.to_dict() 
    

   
