from src.app import app
from flask import render_template
from flask_controller import FlaskController
from flask_login import login_required

class HomeController(FlaskController):
    @app.route('/')
   
    def index():
        return render_template('index.html', titulo_pagina = 'Inicio')

