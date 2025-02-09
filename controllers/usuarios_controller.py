from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.usuarios import Usuarios

class UsuariosController(FlaskController):

    @app.route('/crear_usuario', methods=['POST', 'GET'])
    def crear_usuario():
        usuario = None  # Inicializamos 'usuario' como None antes del renderizado

        if request.method == 'POST':
            # Obtenemos los datos del formulario
            nombre_completo = request.form.get('nombre_completo')
            email = request.form.get('email')
            contrasena = request.form.get('contrasena')
            rol = request.form.get('rol')

            # Creamos un nuevo usuario y lo agregamos
            usuario = Usuarios(nombre_completo=nombre_completo, email=email, contrasena=contrasena, rol=rol)
            Usuarios.agregar_usuario(usuario)  # Suponiendo que este método guarda al usuario
            return redirect(url_for('ver_usuarios'))  # Redirigimos a la página de ver usuarios

        return render_template('formulario_crear_usuario.html', titulo_pagina='Crear Usuario', usuario=usuario)

    @app.route('/ver_usuarios')
    def ver_usuarios():
        # Obtenemos todos los usuarios y los pasamos al template
        usuarios = Usuarios.obtener_usuarios()
        return render_template('tabla_usuarios.html', titulo_pagina='Ver Usuarios', usuarios=usuarios)
    
    

    @app.route('/eliminar_usuario/<id>')
    def eliminar_usuario(id):
        Usuarios.eliminar_usuario(id)
        usuarios = Usuarios.obtener_usuarios()
        return render_template('tabla_usuarios.html', titulo_pagina='Ver Usuarios', usuarios=usuarios)

    @app.route('/actualizar_usuario/<id>', methods=['GET', 'POST'])
    def actualizar_usuario(id):
        if request.method == 'GET':
            # Obtener el usuario por ID
            usuario = Usuarios.obtener_usuario_por_id(id)
            if usuario is None:
                return "Usuario no encontrado", 404

            # Renderizar el formulario de actualización con los datos del usuario
            return render_template(
                'formulario_actualizar_usuario.html',
                titulo_pagina='Actualizar Usuario',
                usuario=usuario
            )

        if request.method == 'POST':
            # Obtener los datos actualizados del formulario
            nombre_completo = request.form.get('nombre_completo')
            email = request.form.get('email')
            contrasena = request.form.get('contrasena')
            rol = request.form.get('rol')

            # Crear un objeto usuario con los datos actualizados
            usuario_actualizado = Usuarios(
                nombre_completo=nombre_completo,
                email=email,
                contrasena=contrasena,
                rol=rol
            )

            # Actualizar el usuario en la base de datos
            Usuarios.actualizar_usuario(usuario_actualizado, id)

            # Redirigir a la página de ver usuarios
            return redirect(url_for('ver_usuarios'))

    @app.route('/consultar_usuario_email/<email>')
    def consultar_usuario_email(email):
        usuario = Usuarios.obtener_usuario_por_email(email)
        return usuario













        

