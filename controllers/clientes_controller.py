from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.clientes import Clientes

class ClientesController(FlaskController):

    @app.route('/crear_cliente', methods=['POST', 'GET'])
    def crear_cliente():
        cliente = None  # Inicializamos 'cliente' como None antes del renderizado
        
        if request.method == 'POST':
            # Obtenemos los datos del formulario
            numero_identificacion = request.form.get('numero_identificacion')
            nombre_completo = request.form.get('nombre_completo')
            direccion = request.form.get('direccion')
            telefono = request.form.get('telefono')
            email = request.form.get('email')

            # Creamos un nuevo cliente y lo agregamos
            cliente = Clientes(numero_identificacion, nombre_completo, direccion, telefono, email)
            Clientes.agregar_cliente(cliente)  # Suponiendo que este método guarda al cliente
            return redirect(url_for('ver_clientes'))  # Redirigimos a la página de ver clientes

        return render_template('formulario_crear_cliente.html', titulo_pagina='Crear Cliente', cliente=cliente)

    @app.route('/ver_clientes')
    def ver_clientes():
        # Obtenemos todos los clientes y los pasamos al template
        clientes = Clientes.obtener_clientes()
        return render_template('tabla_clientes.html', titulo_pagina='Ver Clientes', clientes=clientes)
    

    @app.route('/eliminar_cliente/<id>')
    def eliminar_cliente(id):
        Clientes.eliminar_cliente(id)
        clientes = Clientes.obtener_clientes()
        return render_template('tabla_clientes.html', titulo_pagina='Ver Clientes', clientes=clientes)


    @app.route('/actualizar_cliente/<id>', methods=['GET', 'POST'])
    def actualizar_cliente(id):
        if request.method == 'GET':
            # Obtener el cliente por ID
            cliente = Clientes.obtener_cliente_por_id(id)
            if cliente is None:
                return "Cliente no encontrado", 404
            
            # Renderizar el formulario de actualización con los datos del cliente
            return render_template(
                'formulario_actualizar_cliente.html',
                titulo_pagina='Actualizar Cliente',
                cliente=cliente
            )
        
        if request.method == 'POST':
            # Obtener los datos actualizados del formulario
            numero_identificacion = request.form.get('numero_identificacion')
            nombre_completo = request.form.get('nombre_completo')
            direccion = request.form.get('direccion')
            telefono = request.form.get('telefono')
            email = request.form.get('email')

            # Crear un objeto cliente con los datos actualizados
            cliente_actualizado = Clientes(
                numero_identificacion=numero_identificacion,
                nombre_completo=nombre_completo,
                direccion=direccion,
                telefono=telefono,
                email=email
            )

            # Actualizar el cliente en la base de datos
            Clientes.actualizar_cliente(cliente_actualizado, id)

            # Redirigir a la página de ver clientes
            return redirect(url_for('ver_clientes'))




    @app.route('/consultar_cliente_numero_identificacion/<numero_identificacion>')
    def consultar_cliente_numero_identificacion(numero_identificacion):
        cliente = Clientes.obtener_cliente_por_numero_identificacion(numero_identificacion)
        return cliente


        

