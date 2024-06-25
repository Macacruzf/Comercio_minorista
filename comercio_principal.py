from libreria import iniciar_sesion, agregar_producto, mostrar_inventario, procesar_venta,mostrar_historial_ventas

while True:
    print("\nMenú COMERCIO Alma Zen:")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Procesar venta")
    print("4.Mostrar historial de venta")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        procesar_venta()
    elif opcion == "4":
        mostrar_historial_ventas()
    elif opcion =="5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")


