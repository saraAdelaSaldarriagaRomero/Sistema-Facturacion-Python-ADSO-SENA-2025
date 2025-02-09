from sqlalchemy import Column, Integer, String
from src.models import session, Base

class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre_completo = Column(String(200), nullable=False)
    email = Column(String(500), unique=True, nullable=False)
    contrasena = Column(String(30), nullable=False)
    rol = Column(String(20), nullable=False)

    def __init__(self, nombre_completo, email, contrasena, rol):
        self.nombre_completo = nombre_completo
        self.email = email
        self.contrasena = contrasena
        self.rol = rol

    @staticmethod
    def obtener_usuarios():
        return session.query(Usuarios).all()
    
    def agregar_usuario(usuario):
       usuario = session.add(usuario)
       session.commit()
       return usuario 

    @staticmethod
    def buscar_usuario_por_id(usuario_id):
        return session.query(Usuarios).filter_by(id=usuario_id).first()

    def eliminar_usuario(id):
        usuario = session.query(Usuarios).get(id)        
        session.delete(usuario)
        session.commit()
        return usuario

    def actualizar_usuario(usuario, id):
        # Obtener el usuario existente por ID
        usuario_modificar = session.query(Usuarios).get(id)
        
        if usuario_modificar:
            # Actualizar los atributos del usuario con los nuevos valores
            usuario_modificar.nombre_completo = usuario.nombre_completo
            usuario_modificar.email = usuario.email
            usuario_modificar.contrasena = usuario.contrasena
            usuario_modificar.rol = usuario.rol

            # Guardar los cambios en la base de datos
            session.commit()
            return usuario_modificar
        else:
            return None

    @staticmethod
    def obtener_usuario_por_id(id):
        usuario = session.query(Usuarios).get(id)
        return usuario