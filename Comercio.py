# Inicializar una matriz vacía para almacenar productos (inventario)
inventario = []

# Inicializar una lista para almacenar usuarios
usuarios = []
while True:
    print("Menú COMERCIO ALMA ZEN:")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Procesar venta")
    print("4. Generar informe del inventario")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        inventario.append([nombre, cantidad, precio])
        print(f"Producto '{nombre}' agregado al inventario.")
    elif opcion=="2":
          if inventario:
            print("Inventario:")
            for producto in inventario:
              print(f"Nombre:{producto[0]}, Cantidad:{producto[1]},Precio:${producto[2]:.2f}")
          else:
            print("El inventario está vacío")
