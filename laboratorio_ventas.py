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
        self.__cliente = self.nuevo_cliente(cliente)
        self.__productos_vendidos = self.nuevo_producto(productos_vendidos)

    @property
    def cliente(self):
        return self.__cliente
    
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
    @cliente.setter
    def cliente(self,validar_cliente):
        self.__cliente = self.nuevo_cliente(validar_cliente)

    @productos_vendidos.setter
    def producto(self, validar_producto):
        self.productos_vendidos = self.nuevo_producto(validar_producto)

    def nuevo_cliente(self, cliente):
        try:
            N_cliente = cliente
            if N_cliente != str(cliente):
                raise ValueError('el nombre no lleva numeros desde el if')
            return N_cliente
        except ValueError:
            raise ValueError('el nombre no lleva numeros desde el except')
        
    def nuevo_producto(self, producto): #hay que probar
        try:
            N_producto = producto
            if N_producto != int(producto):
                raise ValueError('el producto no lleva letras desde el if')
            return N_producto
        except ValueError:
            raise ValueError('el producto no lleva letras desde el except')
    
    def __str__(self) -> str:
        return f'{self.fecha}, {self.cliente},{self.productos_vendidos}'
    
class VentaOnline(Venta):
    def __init__(self, fecha, cliente, productos_vendidos,pagina):
        super().__init__(fecha, cliente, productos_vendidos)
        self.__pagina = pagina

    @property
    def pagina(self):
        return self.__pagina

class VentaLocal(Venta):
    def __init__(self, fecha, cliente, productos_vendidos,local):
        super().__init__(fecha, cliente, productos_vendidos)
        self.__local = local

    @property
    def local(self):
        return self.__local

venta = Venta('12/03/2003', 'rodrigo mora', 3)
print(venta) 
venta = venta.nuevo_cliente('hoiad'), venta.nuevo_producto(5)
print(venta)
# venta = venta.nuevo_cliente('asdasd') #aca hay un problema
# print(venta)

'''Desafío 1: Sistema de Gestión de Productos
Objetivo: Desarrollar un sistema para manejar productos en un inventario.

Requisitos:

Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
Implementar operaciones CRUD para gestionar productos del inventario.
Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
Persistir los datos en archivo JSON.'''

# class Producto:
#     def __init__(self, nombre, precio, cantidad_stock):
#         self.__nombre = self.validar_nombre(nombre)
#         self.__precio = self.validar_precio(precio)
#         self.__cantidad_stock = self.validar_cantidad_stock(cantidad_stock)
    
#     @property
#     def nombre(self):
#         return self.__nombre
#     @property
#     def precio(self):
#         return self.__precio
#     @property
#     def cantidad(self):
#         return self.__cantidad_stock

#     @nombre.setter
#     def nombre(self, nuevo_nombre):
#         self.__nombre = self.validar_nombre(nuevo_nombre)

#     @precio.setter
#     def precio(self, validar_precio):
#         self.__precio = self.validar_precio(validar_precio)
        
#     @cantidad.setter
#     def cantidad (self, validar_cantidad_stock):
#         self.__cantidad_stock = self.validar_cantidad_stock(validar_cantidad_stock)

#     def __str__(self) -> str:
#         return f'{self.cantidad}, {self.nombre},{self.precio}'
    
#     def validar_precio(self, precio):
#         try:
#             precio_producto = precio

#             if precio_producto == str(precio):
#                 raise ValueError('el valor debe ser numerico')

#             if precio_producto < 0:
#                 raise ValueError("Monto no disponible, menor a  0 no es valido")
#             return precio_producto
#         except ValueError:
#             raise ValueError("Monto menor a 0 no es valido")
    
#     def validar_cantidad_stock(self, cantidad):
#         try:
#             cantidad_producto = int(cantidad)
#             if len(str(cantidad)) not in [1, 999]:
#                 raise ValueError("Monto no disponible")
#             if cantidad_producto <= 0:
#                 raise ValueError("Monto menor a 0 no disponible")
#             return cantidad_producto
#         except ValueError:
#             raise ValueError("El precio de ser oscilar de 1 a 999 únicamente")
    
#     def validar_nombre(self,nombre):
#         return nombre
        
# producto = Producto('ferrari',80,8)
# print(producto)
# producto = producto.validar_precio(1300)
# print(producto)


# Mostrar información: Imprimir los detalles del producto.
# Actualizar stock: Modificar la cantidad disponible.
# La clase Tienda debe tener un atributo productos (una lista) para almacenar objetos Producto. Además, debe tener métodos para:

# Agregar producto: Crear un validar objeto Producto y agregarlo a la lista.
# Mostrar productos: Imprimir una lista de todos los productos disponibles.
# Buscar producto: Buscar un producto por nombre y devolverlo.
# Actualizar producto: Modificar los atributos de un producto existente.
# Eliminar producto: Eliminar un producto de la lista. 