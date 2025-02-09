from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.facturas import Facturas
from src.models.usuarios import Usuarios


class FacturasController(FlaskController):

    @app.route('/crear_factura', methods=['POST','GET'])
    def crear_factura():    
        if request.method == 'POST':
            numero_factura= request.form.get('numero_factura')
            fecha_factura = request.form.get('fecha_factura')    
            id_cliente = request.form.get('id_cliente')    
            id_usuario = request.form.get('id_usuario')       
            factura = Facturas(numero_factura,fecha_factura,id_cliente,id_usuario)
            Facturas.agregar_factura(factura)
            return redirect(url_for('ver_facturas'))        
        usuarios = Usuarios.obtener_usuarios()
        return render_template('formulario_crear_factura.html', usuarios=usuarios, titulo_pagina = 'Crear Factura')

    @app.route('/ver_facturas')
    def ver_facturas():
        facturas = Facturas.obtener_facturas()
        return render_template('tabla_facturas.html', titulo_pagina = 'Ver Facturas', facturas=facturas)


