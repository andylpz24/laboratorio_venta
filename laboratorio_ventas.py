'''Desafío 2: Sistema de Gestión de Ventas
Objetivo: Desarrollar un sistema para registrar y gestionar ventas de productos.
Requisitos:
Crear una clase base Venta con atributos como fecha, cliente, productos vendidos, etc.
Definir al menos 2 clases derivadas para diferentes tipos de ventas (por ejemplo, VentaOnline, VentaLocal) con atributos y métodos específicos.
Implementar operaciones CRUD para gestionar las ventas.
Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
Persistir los datos en archivo JSON.'''

import json
from datetime import datetime

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

    def nuevo_codigo(self, codigo):
        if not isinstance(codigo, int):
            raise ValueError('El código de venta debe ser un número entero.')
        return codigo
    
    def nueva_fecha(self, fecha):
            try:
                fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
                anio = fecha_objeto.year
                anio_actual = datetime.now().year
                if anio < 1900 or anio > anio_actual:
                    raise ValueError(f'El año debe estar entre 1900 y {anio_actual}.')
                return fecha
            except ValueError as e:
                raise ValueError(f'La fecha debe estar en el formato dd/mm/aaaa. {e}')

    def nuevo_total(self, total):
        if not isinstance(total, float):
            raise ValueError('El código de venta debe ser un número entero.')
        return total
    
    def nuevo_costo(self, costo):
        if not isinstance(costo, float):
            raise ValueError('El código de venta debe ser un número entero.')
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
    def __init__(self, fecha, cliente, productos_vendidos,codigo_venta, total_recaudado, costo ,local):
        super().__init__(fecha, cliente, productos_vendidos,codigo_venta, total_recaudado, costo)
        self.__local = self.nuevo_local(local)

    @property
    def local(self):
        return self.__local

    def to_dict(self):
        data = super().to_dict()
        data['local'] = self.local
        return data
    
    @local.setter
    def local(self, validar_local):
        self.__local = self.nuevo_local(validar_local)

    def nuevo_local(self, local):
        if not isinstance(local, str):
            raise ValueError('El nombre del local debe ser una cadena de texto.')
        if any(char.isdigit() for char in local):
            raise ValueError('El nombre del local no debe contener números.')
        return local

    def __str__(self):
        return (f'{super().__str__()}Local: {self.local}\n'
                '=========================================')

class Gestion():
    def __init__(self, archivo_json):
        self.archivo = archivo_json
    

    def leer_archivo_json(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}  
        except Exception as error:
            raise Exception(f'error al abrir el archivo: {error}')
        else:
            return datos


    def guardar_datos(self,datos):              
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos,file, indent=4)          
        except IOError as error:                
            print(f'error al guardar los datos en {self.archivo}: {error}  (except 1)')
        except Exception as error:
            print(f'error inesperado {error}   (except 2)')
    
    def crear_venta(self, venta):
        try:
            datos = self.leer_archivo_json()
            codigo = venta.codigo_venta
            
            if not str(codigo) in datos.keys():
                datos[codigo] = venta.to_dict()
                self.guardar_datos(datos)
                print('La venta se realizó correctamente.')
            else:
                print(f'El código de venta {codigo} ya existe.')
        except ValueError as error:
            print(f'Error de validación: {error}')
        except Exception as error:
            print(f'Error inesperado al crear venta: {error}')
    
    def encontrar_venta(self, codigo_v):
        try:
            datos = self.leer_archivo_json()       
            codigo_v = str(codigo_v)
            if codigo_v in datos:                   
                venta_data = datos[codigo_v]
                if 'pagina' in venta_data:
                    venta = VentaOnline(**venta_data)     
                else:
                    venta = VentaLocal(**venta_data)
                print(f'venta encontrada exitosamente')
                print(venta)
            else:
                print(f'no se encontro una venta con codigo Nº {codigo_v}')

        except Exception as error:
            print(f'error al encontrar la venta: {error}')

    def eliminar_venta(self, codigo_v):
        try:
            datos = self.leer_archivo_json()
            if str(codigo_v) in datos.keys():
                del datos[codigo_v]
                self.guardar_datos(datos)
                print('venta eliminada')
            else:
                print(f'no se encontro una venta con codigo {codigo_v}')

        except Exception as error:
            print(f'error al eliminar venta: {error}')

    def actualizar_costo(self, codigo, nuevo_costo):
        try:
            datos = self.leer_archivo_json()
            if codigo in datos.keys():
                datos[codigo]['costo'] = nuevo_costo
                self.guardar_datos(datos)
                print(f'se actualizo el costo de la venta con codigo {codigo}')
            else:
                print(f'no se encontro un venta con codigo {codigo}')

        except Exception as error:
            print(f'error encontrado: {error}')


