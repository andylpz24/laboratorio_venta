from laboratorio_ventas import VentaLocal,VentaOnline, Gestion
import os, platform

def limpiar_pantalla():   #limpia la pantalla segun el sistema operativo
    if platform.system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')    #para linux o mac

def mostrar_menu():
    print("========== Menú de Gestión de ventas ==========")
    print('1. Agregar venta online')
    print('2. Agregar venta local')
    print('3. Buscar venta por codigo')
    print('4. Eliminar venta')
    print('5. Mostrar todas las ventas')
    print('6. Salir')
    print('================================================')

def agregar_venta(gestion, tipo_venta):
    while True:
        try:
            while True:
                try:
                    codigo = int(input('Ingresar código de venta: '))
                    break  # Salir del bucle si el dato es válido
                except ValueError:
                    print('Error: El código de venta debe ser un número entero.')

            while True:
                fecha = input('Ingrese fecha de la venta (dd/mm/aaaa): ')
                try:
                    gestion.nueva_fecha(fecha)  # Validar la fecha
                    break  # Salir del bucle si la fecha es válida
                except ValueError as error:
                    print(f'Error: {error}')

            while True:
                cliente = input('Ingresar nombre del cliente: ')
                try:
                    gestion.nuevo_cliente(cliente)  # Validar el nombre del cliente
                    break  # Salir del bucle si el cliente es válido
                except ValueError as error:
                    print(f'Error: {error}')

            while True:
                producto = input('Ingresar nombre del producto: ')
                try:
                    gestion.nuevo_producto(producto)  # Validar el nombre del producto
                    break  # Salir del bucle si el producto es válido
                except ValueError as error:
                    print(f'Error: {error}')

            if tipo_venta == '1':
                while True:
                    pagina = input('Ingresar nombre de la página: ')
                    try:
                        gestion.nueva_pagina(pagina)  # Validar el nombre de la página
                        break  # Salir del bucle si la página es válida
                    except ValueError as error:
                        print(f'Error: {error}')
                
                venta = VentaOnline(fecha, cliente, producto, codigo, pagina)
            
            elif tipo_venta == '2':
                while True:
                    local = input('Ingresar nombre del local: ')
                    try:
                        gestion.nuevo_local(local)  # Validar el nombre del local
                        break  # Salir del bucle si el local es válido
                    except ValueError as error:
                        print(f'Error: {error}')

                venta = VentaLocal(fecha, cliente, producto, codigo, local)
            
            else:
                print('Opción no válida')
                return
            
            gestion.crear_venta(venta)
            print('Venta creada exitosamente.')
            input('Presione una tecla para continuar...')
            break  # Salir del bucle principal después de crear la venta

        except Exception as error:
            print(f'Error inesperado: {error}')

def buscar_venta_por_codigo(gestion):
    codigo = int(input('ingrese el codigo de la venta que quiere buscar: '))
    gestion.encontrar_venta(codigo)
    input('presione un  tecla para limpiar la pantalla: ')

def eliminar_venta_por_codigo(gestion):
    codigo = input('ingrese el codigo de venta a eliminar: ')
    gestion.eliminar_venta(codigo)
    input('presione un  tecla para limpiar la pantalla: ')

def mostrar_todas_las_ventas(gestion):
    print('==============  lista de ventas  ==================')
    for ventas in gestion.leer_archivo_json().values():
        if 'pagina' in ventas:
            print(f"nombre: {ventas['cliente']} - pagina: {ventas['pagina']}" )
        else:
            print(f"nombre: {ventas['cliente']} - local: {ventas['local']}" )
    print('====================================================')
    input('presione un  tecla para limpiar la pantalla: ')

if __name__ == '__main__':                         #--- sirve para leer un archivo py
    archivo_ventas = 'laboratorio_ventas.json'
    gestion_ventas = Gestion(archivo_ventas)

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('elija una opcion: ')

        if opcion == '1' or opcion == '2':
            agregar_venta(gestion_ventas, opcion)
        elif opcion == '3':
            buscar_venta_por_codigo(gestion_ventas)
        elif opcion == '4':
            eliminar_venta_por_codigo(gestion_ventas)
        elif opcion == '5':
            mostrar_todas_las_ventas(gestion_ventas)
        elif opcion == '6':
            print('proceso finalizado')
            break
        else:
            print('opcion no valida')


