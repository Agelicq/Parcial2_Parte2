from crud.cliente_crud import registrar_cliente, clientes_registrados, buscar_por_cedula
from crud.producto_crud import (vender_productos, obtener_producto, mostrar_productos,
    antibioticos_disponibles, fertilizantes_disponibles, productos_control_plagas_disponibles)

def menu_venta():
    cedula = input("Cédula del cliente: ")
    if not (cedula.isdigit() and int(cedula) > 0):
        print("La cédula debe ser un número entero positivo.")
        return

    if cedula not in clientes_registrados:
        print("La cédula ingresada no corresponde a ningún cliente registrado. Regístrelo primero.")
        return

    productos_seleccionados = []

    while True:
        print("\n--- SELECCIÓN DE PRODUCTOS ---")
        print("1. Añadir Antibióticos al carrito")
        print("2. Añadir Fertilizantes al carrito")
        print("3. Añadir un producto de control de Plagas al carrito")
        print("4. Generar factura")
        print("0. Cancelar compra")

        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            print("Compra cancelada.")
            return

        elif opcion == "4":
            if not productos_seleccionados:
                print("No ha seleccionado ningún producto. Debe seleccionar al menos un producto.")
                continue

            fecha = input("Fecha de la compra: ")
            vender_productos(cedula, productos_seleccionados, fecha)
            print("Factura generada exitosamente.")
            return

        elif opcion in ["1", "2", "3"]:
            tipo_producto = {
                "1": "antibiotico",
                "2": "fertilizante",
                "3": "control plagas"
            }[opcion]

            max_items = mostrar_productos(tipo_producto)

            if max_items == 0:
                print("No hay productos disponibles de este tipo.")
                continue

            try:
                seleccion = int(input(f"Seleccione el número del producto (1-{max_items}) o 0 para volver: "))
                if seleccion == 0:
                    continue

                producto = obtener_producto(tipo_producto, seleccion)
                if producto:
                    productos_seleccionados.append(producto)
                    print(f"Producto '{producto.nombre}' añadido al carrito.")
                else:
                    print("Selección inválida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        else:
            print("Opción inválida. Intente nuevamente.")


def menu():
    print("\n!!!Bienvenido al sistema de facturacion de una tienda agricola!!!")
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar Cliente")
        print("2. Realizar Compra/Venta")
        print("3. Buscar Facturas por Cédula")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            while True:
                cedula = input("Cédula del cliente: ")
                if cedula.isdigit() and int(cedula) > 0:
                    break
                else:
                    print("La cédula debe ser un número entero positivo.")
            registrar_cliente(nombre, cedula)

        elif opcion == "2":
            menu_venta()
            input("Presione Enter para continuar...")

        elif opcion == "3":
            while True:
                cedula = input("Ingrese la cédula: ")
                if cedula.isdigit() and int(cedula) > 0:
                    break
                else:
                    print("La cédula debe ser un número entero positivo.")
            buscar_por_cedula(cedula)
            input("Presione Enter para continuar...")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    menu()
