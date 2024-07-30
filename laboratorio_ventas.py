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
    def __init__(self,fecha, cliente, productos_vendidos, codigo_venta):
        self.__fecha = self.nueva_fecha(fecha)
        self.__cliente = self.nuevo_cliente(cliente)     #------ usa la funcion para crear el objeto
        self.__productos_vendidos = self.nuevo_producto(productos_vendidos)
        self.__codigo_venta = self.nuevo_codigo(codigo_venta)

    @property                       #---- property conviente los atributos en propiedad, esto se hace para  no usar objeto.atributo() 
    def cliente(self):              #---- sino que funciona sin () y se puede aplicar logica y consultar/modificar el dato
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

    def to_dict(self):                  #--------------- diccionario para llamar a los atributos de la clase base
        return {
            'fecha' : self.fecha,
            'cliente' : self.cliente,
            'productos_vendidos' : self.productos_vendidos,
            'codigo_venta' : self.codigo_venta
            }

    @cliente.setter                    #---------------- setter es para modificar el atributo
    def cliente(self,validar_cliente):
        self.__cliente = self.nuevo_cliente(validar_cliente) #------------ usa la funcion para actualizar/modificar el objeto

    @productos_vendidos.setter
    def productos_vendidos(self, validar_producto):
        self.__productos_vendidos = self.nuevo_producto(validar_producto)

    @codigo_venta.setter
    def codigo_venta(self,validar_codigo):
        self.__codigo_venta = self.nuevo_codigo(validar_codigo)

    @fecha.setter
    def fecha(self, validar_fecha):
        self.__fecha = self.nueva_fecha(validar_fecha)

    def nuevo_cliente(self, cliente):
        if not isinstance(cliente, str):
            raise ValueError('El nombre del cliente debe ser una cadena de texto.')
        if any(char.isdigit() for char in cliente):
            raise ValueError('El nombre del cliente no debe contener números.')
        return cliente
    
    def nuevo_producto(self, producto):
        if not isinstance(producto, str):
            raise ValueError('El nombre del producto debe ser una cadena de texto.')
        if any(char.isdigit() for char in producto):
            raise ValueError('El nombre del producto no debe contener números.')
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



    def __str__(self):                  #-------------- metodo str para llamar a los atributos en string
        return f'{self.fecha}, {self.cliente},{self.productos_vendidos}, {self.codigo_venta}'

class VentaOnline(Venta):
    def __init__(self, fecha, cliente, productos_vendidos, codigo_venta, pagina):
        super().__init__(fecha, cliente, productos_vendidos, codigo_venta)
        self.__pagina = self.nueva_pagina(pagina)

    @property
    def pagina(self):
        return self.__pagina

    def to_dict(self):                #----------- estudiar este metodo
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
        return f'{super().__str__()} pagina: {self.pagina}'        #----------- estudiar esta linea

class VentaLocal(Venta):
    def __init__(self, fecha, cliente, productos_vendidos,codigo_venta,local):
        super().__init__(fecha, cliente, productos_vendidos,codigo_venta)
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
        return f'{super().__str__()} local: {self.local}'

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
            return {}  # Si el archivo está vacío o no es un JSON válido, devuelve un diccionario vacío
        except Exception as error:
            raise Exception(f'error al abrir el archivo: {error}')
        else:
            return datos


    def guardar_datos(self,datos):               #------------ probar y estudiar
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos,file, indent=4)          #-------- dump es lo opuesto a load, convierte un objeto python a uno json para modificarlo     
        except IOError as error:                 #---------------------- estudiar esta linea (probar otro nomre en IOError)
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
            datos = self.leer_archivo_json()         # '''no se encuenta el dato al usar la opcion 3
            codigo_v = str(codigo_v)
            if codigo_v in datos:                    # ----------- posible error en nombre de variable codigo_v
                venta_data = datos[codigo_v]
                if 'pagina' in venta_data:
                    venta = VentaOnline(**venta_data)     #------ ** significa que es o pasa un diccionario 
                else:
                    venta = VentaLocal(**venta_data)
                print(f' venta con codigo {codigo_v} encontrada')
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


