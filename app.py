from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from src.models import Base, engine, Usuarios
from flask_controller import FlaskControllerRegister
from flask_cors import CORS

app = Flask(__name__)
CORS(app)







# Configurar la clave secreta y habilitar el modo de depuración
app.secret_key = "mi_llaveria"
app.debug = True

# Inicializar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)  # Asocia Flask-Login con la app
login_manager.login_view = "login"  # Página a la que se redirige si el usuario no está autenticado

# Función de carga de usuarios para Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return Usuarios.obtener_usuario_por_id(user_id)

# Registrar los controladores usando FlaskControllerRegister
register = FlaskControllerRegister(app)
register.register_package('src.controllers')

# Crear todas las tablas en la base de datos si aún no existen
Base.metadata.create_all(engine)

# Asegurar que la aplicación solo se ejecute si es el archivo principal
if __name__ == '__main__':
    app.run(debug=True)



"""

from flask import Flask
from src.models import Base, engine
from flask_controller import FlaskControllerRegister

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar la clave secreta y habilitar el modo de depuración
app.secret_key = "mi_llaveria"
app.debug = True

# Registrar los controladores usando FlaskControllerRegister
register = FlaskControllerRegister(app)
register.register_package('src.controllers')

# Crear todas las tablas en la base de datos, si aún no existen
Base.metadata.create_all(engine)

# Asegúrate de que la aplicación solo se ejecute si es el archivo principal
if __name__ == '__main__':
    # Ejecutar la aplicación Flask en modo desarrollo
    app.run(debug=True)
"""