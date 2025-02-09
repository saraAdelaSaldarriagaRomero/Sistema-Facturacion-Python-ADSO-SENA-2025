

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

