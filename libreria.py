# Comercio_libreria.py

# Usuario
nombre_usuario = "user"
contraseña = "1111"

def iniciar_sesion():
    intentos = 3
    while intentos > 0:
        usuario_ingresado = input("Nombre de usuario: ")
        contraseña_ingresada = input("Contraseña: ")
        if usuario_ingresado == nombre_usuario and contraseña_ingresada == contraseña:
            print("Inicio de sesión exitoso. ¡Bienvenido!")
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")
            intentos -= 1
    print("Número de intentos agotados. Por favor, inténtelo más tarde.")
    return False

# Inventario
inventario = []
historial_ventas = []

def agregar_producto():
    while True:
        print("====== Agregar Producto ======")
        print("1. Agregar un nuevo producto")
        print("2. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            codigo = input("Ingrese el código del producto (4 dígitos): ")
            if codigo.isdigit() and len(codigo) == 4:
                nombre = input("Ingrese el nombre del producto: ")
                while True:
                    cantidad = input("Ingrese la cantidad del producto: ")
                    if cantidad.isdigit():
                        cantidad = int(cantidad)
                        while True:
                            precio = input("Ingrese el precio del producto: ")
                            if precio.replace(".", "", 1).isdigit():
                                precio = float(precio)
                                inventario.append([int(codigo), nombre, cantidad, precio])
                                print(f"Producto '{nombre}' agregado al inventario.")
                                break
                            else:
                                print("Error: El precio debe ser un número. Por favor, inténtelo de nuevo.")
                        break
                    else:
                        print("Error: La cantidad debe ser un número entero. Por favor, inténtelo de nuevo.")
            else:
                print("Error: El código debe ser un número entero de 4 dígitos. Por favor, inténtelo de nuevo.")
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")

def mostrar_inventario():
    while True:
        print("====== Mostrar Inventario ======")
        print("1. Mostrar inventario")
        print("2. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            if inventario:
                print("Inventario:")
                for producto in inventario:
                    codigo, nombre, cantidad, precio_unitario = producto
                    total_valor = cantidad * precio_unitario
                    print(f"Código: {codigo}, Nombre: {nombre}, Cantidad: {cantidad}, Precio unitario: ${precio_unitario:.2f}, Total valor: ${total_valor:.2f}")
            else:
                print("El inventario está vacío.")
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")

def procesar_venta():
    while True:
        print("====== Procesar Venta ======")
        print("1. Procesar una venta")
        print("2. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            if nombre_producto:
                cantidad_a_vender = input("Ingrese la cantidad a vender: ")
                if cantidad_a_vender.isdigit():
                    cantidad_a_vender = int(cantidad_a_vender)
                    for producto in inventario:
                        if producto[1] == nombre_producto:
                            if producto[2] >= cantidad_a_vender:
                                producto[2] -= cantidad_a_vender
                                precio_sin_iva = producto[3] * cantidad_a_vender
                                precio_con_iva = precio_sin_iva * 1.19  # impuesto de IVA
                                historial_ventas.append([nombre_producto, cantidad_a_vender, precio_con_iva])
                                print("----Boleta----")
                                print(f"Venta procesada: Se vendieron {cantidad_a_vender} unidades de '{nombre_producto}'.")
                                print(f"Total: ${precio_con_iva:.2f} (IVA 19% incluido).")
                                break
                            elif producto[2] < cantidad_a_vender:
                                print(f"No hay suficientes unidades de '{nombre_producto}' en stock.")
                                break
                    else:
                        print(f"El producto '{nombre_producto}' no está en el inventario.")
                else:
                    print("Error: La cantidad debe ser un número entero.")
            else:
                print("Error: El nombre del producto no puede estar vacío.")
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")

def mostrar_historial_ventas():
    while True:
        print(" ====== Mostrar Historial de Ventas ======")
        print("1. Mostrar historial de ventas")
        print("2. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            if historial_ventas:
                print("Historial de ventas:")
                for venta in historial_ventas:
                    nombre_producto, cantidad, total = venta
                    print(f"Producto: {nombre_producto}, Cantidad: {cantidad}, Total: ${total:.2f}")
            else:
                print("No hay ventas registradas.")
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")

       




       




       



