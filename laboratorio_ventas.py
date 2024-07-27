'''Desafío 2: Sistema de Gestión de Ventas
Objetivo: Desarrollar un sistema para registrar y gestionar ventas de productos.
Requisitos:
Crear una clase base Venta con atributos como fecha, cliente, productos vendidos, etc.
Definir al menos 2 clases derivadas para diferentes tipos de ventas (por ejemplo, VentaOnline, VentaLocal) con atributos y métodos específicos.
Implementar operaciones CRUD para gestionar las ventas.
Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
Persistir los datos en archivo JSON.'''

import json

class Venta():
    def __init__(self,fecha, cliente, productos_vendidos, codigo_venta):
        self.__fecha = fecha
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
            'productos vendidos' : self.productos_vendidos,
            'codigo de venta' : self.codigo_venta
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

    def nuevo_cliente(self, cliente):   #------------- es funcion para validar el tipo de dato, la misma que recibe el atributo original su el setter       
        try:
            N_cliente = cliente                      # tener cuidado con esta linea y la siguiente que puede tener errores comunes
            if N_cliente != str(cliente):
                raise ValueError('el nombre del cliente no lleva numeros desde el if')
            return N_cliente
        except ValueError:
            raise ValueError('el nombre del cliente lleva numeros desde el except')

    def nuevo_producto(self, producto): 
        try:
            N_producto = producto
            if N_producto != str(producto):
                raise ValueError('el nombre del producto no lleva numeros (desde if)')
            return N_producto
        except ValueError:
            raise ValueError('el nombre del producto no lleva numeros (desde except)')

    def nuevo_codigo(self, codigo):
        try:
            N_codigo = codigo
            if N_codigo != int(codigo):
                raise ValueError('el codigo de venta no lleva letras (desde if)')
            return N_codigo
        except ValueError:
            raise ValueError('el codigo de venta no lleva letras (desde except)')

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
        try:
            N_pagina = pagina
            if N_pagina != str(pagina):
                raise ValueError('valor no valido (desde if)')
            return  N_pagina
        except Exception as error:
            print(f'error inesperado: {error} (desde except)')

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
        try:
            N_local = local
            if N_local != str(local):
                raise ValueError('valor no valido (desde if)')
            return  N_local
        except Exception as error:
            print(f'error inesperado: {error} (desde except)')
    
    def __str__(self):
        return f'{super().__str__()} local: {self.local}'

class Gestion():
    def __init__(self, archivo_json):
        self.archivo = archivo_json
    
    def leer_archivo_json(self):          #---------- probar y estudiar
        try:
            with open(self.archivo, 'r') as file:    #-------- abre un archivo, 'r' (lee el archivo) y lo guarda en una variable
                datos = json.load(file)              #-------- json.load() se usa para que python lo pueda manejar al archivo json
        except FileNotFoundError:
            return {}
        except Exception as error:                   #-------- error es una variable que guarda exception
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

    def crear_venta(self, codigo_v):             #------------ posible error desde el main 'agregar_venta()'
        try:
            datos = self.leer_archivo_json()
            codigo = codigo_v.codigo_venta
            if not str(codigo) in datos.keys():
                datos[codigo] = codigo_v.to_dict()
                self.guardar_datos(datos)              #--------- revisar la linea de abajo, porsible error en producto
                print(f'la venta se realizo correctamente (desde if)') #''' se ejecuta al usar la opcion 2'''
            else:
                print(f'codigo {codigo} (desde else)')    #'''se ejecuta este codigo al usar la opcion 1, revisar'''
        except Exception as error:
            print(f'Error inesperado al crear venta: {error}  (desde except)')

    def encontrar_venta(self, codigo_v):
        try:
            datos = self.leer_archivo_json()         # '''no se encuenta el dato al usar la opcion 3
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
            if str(codigo_v) in datos.keys:
                del datos[codigo_v]
                self.guardar_datos(datos)
                print('venta eliminada')
            else:
                print(f'no se encontro una venta con codigo {codigo_v}')

        except Exception as error:
            print(f'error al eliminar venta: {error}')





'''
i usually wake up at 8 a.m and then drink a coffee, 
depends of the day i have online classes or i review last class before to start practice,
sometimes i study a bit of microsoft azure on codigofacilito, i dont have time to study many things,
but i hope to get a certified on azure developer associate, in the afthernoon
i always study some of data analytic on informatorio and in the evening i work on perfecting my english with technical english course
'''

