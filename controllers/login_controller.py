from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.usuarios import Usuarios
from flask_login import login_user

class LoginController(FlaskController):
    @app.route('/', methods=['POST', 'GET'])
    def login():    
        if request.method == 'POST':
            email = request.form.get('email')                
            contrasena = request.form.get('contrasena')    

            # Asegurarse de que `validar_usuario` devuelve un objeto usuario, no un booleano
            usuario_valido = Usuarios.validar_usuario(email, contrasena)

            if usuario_valido:  # Si el usuario existe
                login_user(usuario_valido)  # Flask-Login manejará la sesión
                return redirect(url_for('ver_productos'))  # Redirige a otra vista
            
           
            return redirect(url_for('index'))  # Redirige a la página de login

        return render_template('index.html', titulo_pagina='index')


"""

from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.usuarios import Usuarios
from flask_login import login_user

class LoginController(FlaskController):
    @app.route('/login', methods=['POST','GET'])
    def login():    
        if request.method == 'POST':
            email = request.form.get('email')                
            contrasena = request.form.get('contrasena')    
            usuario_valido = Usuarios.validar_usuario(email, contrasena)
            if usuario_valido:
                login_user(usuario_valido)
                return redirect(url_for('index'))
            return redirect(url_for('login'))
        return render_template('formulario_login.html', titulo_pagina = 'Login')
"""