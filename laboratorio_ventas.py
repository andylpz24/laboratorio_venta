'''Desafío 2: Sistema de Gestión de Ventas
Objetivo: Desarrollar un sistema para registrar y gestionar ventas de productos.
Requisitos:
Crear una clase base Venta con atributos como fecha, cliente, productos vendidos, etc.
Definir al menos 2 clases derivadas para diferentes tipos de ventas (por ejemplo, VentaOnline, VentaLocal) con atributos y métodos específicos.
Implementar operaciones CRUD para gestionar las ventas.
Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
Persistir los datos en archivo JSON.'''

import json
from decimal import Decimal
from datetime import datetime
import mysql.connector
from mysql.connector import Error
from decouple import config

class Venta():
    def __init__(self,fecha, cliente, productos_vendidos, codigo_venta, total_recaudado, costo):
        self.__fecha = self.nueva_fecha(fecha)
        self.__cliente = self.nuevo_cliente(cliente)     
        self.__productos_vendidos = self.nuevo_producto(productos_vendidos)
        self.__codigo_venta = self.nuevo_codigo(codigo_venta)
        self.__total_recaudado = self.nuevo_total(total_recaudado)
        self.__costo = self.nuevo_costo(costo)

    @property                      
    def cliente(self):              
        return self.__cliente

    @property
    def fecha(self):
        return self.__fecha

    @property
    def productos_vendidos(self):
        return self.__productos_vendidos

    @property
    def codigo_venta(self):
        return self.__codigo_venta
    
    @property
    def total_recaudado(self):
        return self.__total_recaudado
    
    @property
    def costo(self):
        return self.__costo

    def to_dict(self):                 
        return {
            'fecha' : self.fecha,
            'cliente' : self.cliente,
            'productos_vendidos' : self.productos_vendidos,
            'codigo_venta' : self.codigo_venta,
            'total_recaudado' : self.total_recaudado,
            'costo' : self.costo
            }

    @cliente.setter                   
    def cliente(self,validar_cliente):
        self.__cliente = self.nuevo_cliente(validar_cliente) 

    @productos_vendidos.setter
    def productos_vendidos(self, validar_producto):
        self.__productos_vendidos = self.nuevo_producto(validar_producto)

    @codigo_venta.setter
    def codigo_venta(self,validar_codigo):
        self.__codigo_venta = self.nuevo_codigo(validar_codigo)

    @fecha.setter
    def fecha(self, validar_fecha):
        self.__fecha = self.nueva_fecha(validar_fecha)

    @total_recaudado.setter
    def total_recaudado(self, validar_total):
        self.__total_recaudado = self.nuevo_total(validar_total)

    @costo.setter
    def costo(self, validar_costo):
        self.__costo = self.nuevo_costo(validar_costo)

    def nuevo_cliente(self, cliente):
        if not isinstance(cliente, str):
            raise ValueError('El nombre del cliente debe ser una cadena de texto.')
        if any(char.isdigit() for char in cliente):
            raise ValueError('El nombre del cliente no debe contener números.')
        return cliente
    
    def nuevo_producto(self, producto):
        if not isinstance(producto, str):
            raise ValueError('El nombre del producto debe ser una cadena de texto.')
        return producto

    def nuevo_codigo(self, codigo_venta):
        if not isinstance(codigo_venta, int):
            raise ValueError('El código de venta debe ser un número entero.')
        return codigo_venta

    def nueva_fecha(self, fecha):
        try:
            if isinstance(fecha, datetime):  # Verifica si fecha es un objeto datetime
                fecha_convertida = fecha.strftime("%Y-%m-%d")
            else:
                fecha_objeto = datetime.strptime(fecha, "%Y-%m-%d")   # Intenta analizar la fecha en el formato 'YYYY-MM-DD'
                anio = fecha_objeto.year         # Verifica que el año esté en el rango válido
                anio_actual = datetime.now().year
                if anio < 1900 or anio > anio_actual:
                    raise ValueError(f'El año debe estar entre 1900 y {anio_actual}.')
                fecha_convertida = fecha_objeto.strftime("%Y-%m-%d")

            return fecha_convertida
        except ValueError as e:
            raise ValueError(f'La fecha debe estar en el formato yyyy-mm-dd. {e}')


    def nuevo_total(self, total):
        if not isinstance(total, (Decimal, float)):
            raise ValueError('El total debe ser un número decimal.')
        return total

    def nuevo_costo(self, costo):
        if not isinstance(costo, (float, Decimal)):
            raise ValueError('El costo debe ser un número decimal.')
        return costo

    def __str__(self):
        return ('=========================================== \n'
                f'Código de venta: {self.codigo_venta}\n'
                f'Cliente: {self.cliente}\n'
                f'Producto: {self.productos_vendidos}\n'
                f'Fecha: {self.fecha}\n'
                f'Total recaudado: {self.total_recaudado}\n'
                f'Costo: {self.costo}\n')

class VentaOnline(Venta):
    def __init__(self, fecha, cliente, productos_vendidos, codigo_venta, total_recaudado, costo, pagina):
        super().__init__(fecha, cliente, productos_vendidos, codigo_venta, total_recaudado, costo)
        self.__pagina = self.nueva_pagina(pagina)

    @property
    def pagina(self):
        return self.__pagina

    def to_dict(self):               
        data = super().to_dict()
        data['pagina'] = self.pagina
        return data
    
    @pagina.setter
    def pagina(self, validar_pagina):
        self.__pagina = self.nueva_pagina(validar_pagina)

    def nueva_pagina(self, pagina):
        if not isinstance(pagina, str):
            raise ValueError('El nombre de la pagina debe ser una cadena de texto.')
        if any(char.isdigit() for char in pagina):
            raise ValueError('El nombre de la pagina no debe contener números.')
        return pagina

    def __str__(self):
        return (f'{super().__str__()}Pagina: {self.pagina}\n'       
                '===========================================')

class VentaLocal(Venta):
    def __init__(self, fecha, cliente, productos_vendidos,codigo_venta, total_recaudado, costo ,local_):
        super().__init__(fecha, cliente, productos_vendidos,codigo_venta, total_recaudado, costo)
        self.__local_ = self.nuevo_local(local_)

    @property
    def local_(self):
        return self.__local_

    def to_dict(self):
        data = super().to_dict()
        data['local_'] = self.local_
        return data
    
    @local_.setter
    def local_(self, validar_local):
        self.__local_ = self.nuevo_local(validar_local)

    def nuevo_local(self, local_):
        if not isinstance(local_, str):
            raise ValueError('El nombre del local debe ser una cadena de texto.')
        if any(char.isdigit() for char in local_):
            raise ValueError('El nombre del local no debe contener números.')
        return local_

    def __str__(self):
        return (f'{super().__str__()}Local: {self.local_}\n'
                '=========================================')

class Gestion():
    def __init__(self):
        self.host = config('db_host')
        self.database = config('db_name')
        self.user = config('db_user')
        self.password = config('db_password')
        self.port = config('db_port')
    
    def connect(self):    # establece conexcion con la db
        try:
            connection = mysql.connector.connect(
                host = self.host,
                database = self.database,
                user = self.user,
                password =self.password,
                port = self.port
            )

            if connection.is_connected():
                return connection

        except Error as e:
            print(f'error al conectar la base de datos: {e}')
            return None

    def crear_venta(self, venta):
        try:
            connection = self.connect()
            if connection:
                with connection.cursor() as cursor:    
                    cursor.execute('SELECT codigo_venta FROM venta WHERE codigo_venta = %s' ,(venta.codigo_venta,))  # -----------verifica si existe un codigo de venta 
                    if cursor.fetchone():     # -----------busca un registro
                        print(f'Error: ya existe esa venta con codigo: {venta.codigo_venta}')
                        return

                    convertir_fecha = venta.nueva_fecha(venta.fecha)

                    if isinstance(venta, VentaLocal):    # --------- inserar  venta dependiendo del tipo
                        query = '''
                        INSERT INTO venta (codigo_venta, cliente, productos_vendidos, fecha, total_recaudado, costo)
                        VALUES (%s,%s,%s,%s,%s,%s)
                        '''
                        cursor.execute(query,(venta.codigo_venta, 
                                            venta.cliente, 
                                            venta.productos_vendidos, 
                                            convertir_fecha, 
                                            venta.total_recaudado, 
                                            venta.costo))
                        
                        query = '''
                        INSERT INTO venta_local (codigo_venta, local_)
                        VALUES (%s, %s)
                        '''
                        cursor.execute(query, (venta.codigo_venta, venta.local_))

                    elif isinstance(venta, VentaOnline):   
                        query = '''
                        INSERT INTO venta (codigo_venta, cliente, productos_vendidos, fecha, total_recaudado, costo)
                        VALUES (%s,%s,%s,%s,%s,%s)
                        '''
                        cursor.execute(query,(venta.codigo_venta, 
                                            venta.cliente, 
                                            venta.productos_vendidos, 
                                            convertir_fecha, 
                                            venta.total_recaudado, 
                                            venta.costo))
                        
                        query = '''
                        INSERT INTO venta_online (codigo_venta, pagina)
                        VALUES (%s, %s) 
                        '''
                        cursor.execute(query, (venta.codigo_venta, venta.pagina))

                    connection.commit()     # ----- guarda la consulta en la db
                    print(f'venta con codigo Nº: {venta.codigo_venta} creado exitosamente')

        except ValueError as error:
            print(f'Error de validación: {error}')
        except Exception as e:
            print(f'Error inesperado al crear venta: {e}')

    def encontrar_venta(self, codigo_venta):
        try:
            # breakpoint()
            connection = self.connect()
            with connection.cursor(dictionary=True) as cursor:
                # Agrega la línea de depuración aquí
                print(f'Tipo de codigo_venta: {type(codigo_venta)}, Valor: {codigo_venta}')
                
                cursor.execute('SELECT * FROM venta WHERE codigo_venta = %s', (codigo_venta,))
                venta_data = cursor.fetchone()

                if venta_data:
                    cursor.execute('SELECT pagina FROM venta_online WHERE codigo_venta = %s', (codigo_venta,))
                    
                    pagina = cursor.fetchone()

                    if pagina:
                        venta_data['pagina'] = pagina['pagina']
                        venta = VentaOnline(**venta_data)
                    
                    else:
                        cursor.execute('SELECT local_ FROM venta_local WHERE codigo_venta = %s', (codigo_venta,))
                        local = cursor.fetchone()

                        if local:
                            venta_data['local_'] = local['local_']
                            venta = VentaLocal(**venta_data)    

                        else:
                            venta = Venta(**venta_data)                        
                    print(f'venta Nº: {venta} encontrada')

                else:
                    print(f'No se encontró la venta con código Nº: {codigo_venta}')

        except Exception as error:
            import logging
            logging.error(error, exc_info=True)
            # print(f'Error al encontrar la venta: {error}')

        finally:
            if connection.is_connected():
                connection.close()

    def eliminar_venta(self, codigo_venta):
        try:
            connnetion = self.connect()
            if connnetion:
                with connnetion.cursor() as cursor:
                    cursor.execute('SELECT * FROM venta WHERE codigo_venta = %s', ((codigo_venta),))
                    if not cursor.fetchone():
                        print(f'no se encontro una venta con codigo: {codigo_venta}')
                        return
                    
                    #eliminar la venta
                    cursor.execute('DELETE FROM venta_online WHERE codigo_venta = %s', (codigo_venta,))
                    cursor.execute('DELETE FROM venta_local WHERE codigo_venta = %s', (codigo_venta,))
                    cursor.execute('DELETE FROM venta WHERE codigo_venta = %s', (codigo_venta,))
                    if cursor.rowcount > 0:
                        connnetion.commit()
                        print(f'venta con codigo: {codigo_venta} borrada')
                    else:
                        print(f'no se encontro una venta con codigo: {codigo_venta}')

        except Exception as e:
            print(f'error al borrar la venta: {e}')
        finally:
            if connnetion.is_connected():
                connnetion.close()

    def actualizar_costo(self, codigo_venta, nuevo_costo):
        try:
            connection = self.connect()
            if connection:
                with connection.cursor() as cursor:   # -------verifica si existe codigo de venta
                    cursor.execute('SELECT * FROM venta WHERE codigo_venta = %s',(codigo_venta,))

                    if not cursor.fetchone():
                        print(f'no se escontro un venta con codigo: {codigo_venta}')
                        return
                    # actualiza el costo
                    cursor.execute('UPDATE venta SET costo = %s WHERE codigo_venta = %s',
                    (nuevo_costo, codigo_venta))

                    if cursor.rowcount > 0:
                        connection.commit()
                        print('====================================================\n'
                            f'el costo de la venta Nº {codigo_venta} se actualizo. \n'
                            f'el nuevo costo es: {nuevo_costo}')
                    else:
                        print(f'no se encontro la venta con codigo: {codigo_venta}')
        except Exception as e:
            print(f'error al actualizar el costo de evnta: {e}')
        finally:
            if connection.is_connected:
                connection.close()

    def mostrar_todas_las_ventas(self):
        try:
            connection = self.connect()
            if connection:
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute('SELECT * FROM venta')
                    ventas_data = cursor.fetchall()
                    ventas = []

                    for venta_data in ventas_data:
                        codigo_venta = venta_data['codigo_venta']
                        cursor.execute('SELECT local_ FROM venta_local WHERE codigo_venta = %s',(codigo_venta,))
                        local = cursor.fetchone()

                        if local:
                            venta_data['local_'] = local['local_']
                            venta = VentaLocal(**venta_data)
                        else:
                            cursor.execute('SELECT pagina FROM venta_online WHERE codigo_venta = %s',(codigo_venta,))
                            pagina = cursor.fetchone()
                            venta_data['pagina'] = pagina['pagina']
                            venta = VentaOnline(**venta_data)
                        
                        ventas.append(venta)

        except Exception as e:
            print(f'error al mostrar las ventas: {e}')
        else:
            return ventas
        finally:
            if connection.is_connected():
                connection.close()






