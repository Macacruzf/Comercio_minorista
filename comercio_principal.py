from Comercio_libreria import iniciar_sesion, agregar_producto, mostrar_inventario, procesar_venta

def mostrar_menu():
    print("\nMenu Comercio ALMA ZEN")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Procesar venta")
    print("4. Salir")

def main():
    if iniciar_sesion():
        while True:
            mostrar_menu()
            opcion = input("Ingrese una opción (1-5): ")
            if opcion == "1":
                agregar_producto()
            elif opcion == "2":
                mostrar_inventario()
            elif opcion == "3":
                procesar_venta()

            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    main()

