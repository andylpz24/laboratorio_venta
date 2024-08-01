from laboratorio_ventas import VentaLocal,VentaOnline, Gestion
import os, platform

def limpiar_pantalla():  
    if platform.system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')   

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
            codigo = int(input('ingrese el codigo de venta (debe ser un numero entero) :'))
            cliente = input('ingrese el nombre del cliente: ')
            producto = input('ingrese el nombre del producto: ')
            fecha = input('ingrese la fecha (debe estar en formato dd/mm/aaaa): ')
            total = float(input('ingrese el total de venta recaudado: '))
            costo = float(input('ingrese el costo de venta: '))

            if tipo_venta == '1':
                pagina = input('Ingresar nombre de la página: ')
                venta = VentaOnline(fecha, cliente, producto, codigo,total, costo, pagina)
            
            elif tipo_venta == '2':
                local = input('Ingresar nombre del local: ')
                venta = VentaLocal(fecha, cliente, producto, codigo, total, costo, local)
            
            else:
                print('Opción no válida')
                return
            
            gestion.crear_venta(venta)
            print('Venta creada exitosamente.')
            input('Presione una tecla para continuar...')
            break  

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

def actualizar_costo(gestion):
    codigo = input('ingrese codigo de venta para actualizar el costo: ')
    costo = float(input('ingrese el costo de venta: '))
    gestion.actualizar_costo(codigo, costo)
    input('presione un  tecla para limpiar la pantalla: ')

def mostrar_todas_las_ventas(gestion):
    print('==============  Lista de Ventas  ==================')
    
    ventas_data = gestion.leer_archivo_json()
    
    for venta_data in ventas_data.values():
    
        if 'pagina' in venta_data:
        
            venta = VentaOnline(
                fecha=venta_data['fecha'],
                cliente=venta_data['cliente'],
                productos_vendidos=venta_data['productos_vendidos'],
                codigo_venta=venta_data['codigo_venta'],
                total_recaudado=venta_data['total_recaudado'],
                costo=venta_data['costo'],
                pagina=venta_data['pagina']
            )
        else:
            
            venta = VentaLocal(
                fecha=venta_data['fecha'],
                cliente=venta_data['cliente'],
                productos_vendidos=venta_data['productos_vendidos'],
                codigo_venta=venta_data['codigo_venta'],
                total_recaudado=venta_data['total_recaudado'],
                costo=venta_data['costo'],
                local=venta_data['local']
            )
        
        print(venta)  

    print('====================================================')
    input('Presione una tecla para limpiar la pantalla: ')

if __name__ == '__main__':                         
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
            actualizar_costo(gestion_ventas)
        elif opcion == '7':
            print('proceso finalizado')
            break
        else:
            print('opcion no valida')
