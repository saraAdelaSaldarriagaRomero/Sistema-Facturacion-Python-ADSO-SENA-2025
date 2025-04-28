# Importamos la instancia de la aplicación Flask desde el módulo src.app
from src.app import app

# Importamos módulos de Flask para manejar rutas, solicitudes y redirecciones
from flask import render_template, request, redirect, url_for

# Importamos FlaskController, que es una clase base para organizar controladores
from flask_controller import FlaskController

# Importamos el modelo Categorias, que nos permite interactuar con la base de datos de categorías
from src.models.categorias import Categorias

# Definimos la clase CategoriasController, que manejará las operaciones relacionadas con categorías
class CategoriasController(FlaskController):

    # Definimos una ruta en la aplicación para obtener la lista de categorías
    @app.route('/ver_categorias')
    def obtener_lista_categorias():
        # Llamamos al método obtener_categorias() de la clase Categorias para obtener todas las categorías almacenadas
        categorias = Categorias.obtener_categorias()
        
        # Devolvemos la lista de categorías obtenida. 
        # Nota: No se está renderizando una plantilla ni convirtiendo en JSON, lo que podría causar problemas al devolver la respuesta.
        return categorias
