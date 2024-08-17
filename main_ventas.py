from laboratorio_ventas import VentaLocal,VentaOnline, Gestion
import os, platform

def limpiar_pantalla():  
    if platform.system() == 'windows':
        os.system('cls')

def mostrar_menu():
    print("========== Menú de Gestión de ventas ==========")
    print('1. Agregar venta online')
    print('2. Agregar venta local')
    print('3. Buscar venta por codigo')
    print('4. Eliminar venta')
    print('5. Mostrar todas las ventas')
    print('6. Actualizar costo de venta')
    print('7. Salir')
    print('================================================')

def agregar_venta(gestion, tipo_venta):
    while True:
        try:
            codigo_venta = int(input('ingrese el codigo de venta (debe ser un numero entero): '))
            cliente = input('ingrese el nombre del cliente: ')
            producto = input('ingrese el nombre del producto: ')
            fecha = input('ingrese la fecha (separardo por -): ')
            total = float(input('ingrese el total de venta recaudado: '))
            costo = float(input('ingrese el costo de venta: '))

            if tipo_venta == '1':
                pagina = input('Ingresar nombre de la página: ')
                venta = VentaOnline(fecha, cliente, producto, codigo_venta,total, costo, pagina)
            
            elif tipo_venta == '2':
                local_ = input('Ingresar nombre del local: ')
                venta = VentaLocal(fecha, cliente, producto, codigo_venta, total, costo, local_)
            
            else:
                print('Opción no válida')
                return
            
            gestion.crear_venta(venta)
            input('Presione una tecla para continuar...')
            break  

        except Exception as error:
            print(f'Error inesperado: {error}')

def buscar_venta_por_codigo(gestion):
    codigo_venta = int(input('ingrese el codigo de la venta que quiere buscar: '))
    gestion.encontrar_venta(codigo_venta)
    input('presione un  tecla para limpiar la pantalla: ')

def eliminar_venta_por_codigo(gestion):
    codigo = input('ingrese el codigo de venta a eliminar: ')
    gestion.eliminar_venta(codigo)
    input('presione un  tecla para limpiar la pantalla: ')

def actualizar_costo(gestion):
    codigo = input('ingrese codigo de venta para actualizar el costo: ')
    costo = float(input('ingrese el costo de venta: '))
    gestion.actualizar_costo(codigo, costo)
    input('presione un  tecla para limpiar la pantalla: ')

def mostrar_todas_las_ventas(gestion):
    print('==============  Lista de Ventas  ==================')
    try:
        ventas = gestion.mostrar_todas_las_ventas()
        for venta in ventas:
            if isinstance(venta, VentaLocal):
                print('-----------------------------------------\n'
                    f'tipo de venta: venta local \n'
                    f'codigo de venta: {venta.codigo_venta}\n'
                    f'nombre del cliente: {venta.cliente}\n'
                    f'local: {venta.local_}')
                
            elif isinstance(venta, VentaOnline):
                print('-----------------------------------------\n'
                    f'tipo de venta: venta online \n'
                    f'codigo de venta: {venta.codigo_venta}\n'
                    f'nombre del cliente: {venta.cliente}\n'
                    f'pagina: {venta.pagina}')

    except Exception as e:
        print(f'error al mostrar todas las ventas: {e}')

    print('====================================================')
    input('Presione una tecla para limpiar la pantalla: ')

if __name__ == '__main__':                         
    gestion_ventas = Gestion()

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
            actualizar_costo(gestion_ventas)
        elif opcion == '7':
            print('proceso finalizado')
            break
        else:
            print('opcion no valida')



