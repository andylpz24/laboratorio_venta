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
    def __init__(self,fecha,cliente,productos_vendidos):
        self.__fecha = fecha
        self.__cliente = cliente
        self.__productos_vendidos = productos_vendidos

    @property
    def cliente(self):
        return self.__cliente.capitalize()
    
    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def productos_vendidos(self):
        return self.__productos_vendidos
    
    def to_dict(self):
        return {
            'fecha' : self.fecha,
            'cliente' : self.cliente,
            'productos vendidos' : self.productos_vendidos
            }
    

class VentaOnline(Venta):
    def __init__(self, fecha, cliente, productos_vendidos,pagina):
        super().__init__(fecha, cliente, productos_vendidos)
        self.__pagina = pagina

    @property
    def pagina(self):
        return self.__pagina.capitalize()

class VentaLocal(Venta):
    def __init__(self, fecha, cliente, productos_vendidos,local):
        super().__init__(fecha, cliente, productos_vendidos)
        self.__local = local

    @property
    def local(self):
        return self.__local.capitalize()
