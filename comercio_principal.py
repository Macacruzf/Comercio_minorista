from libreria import agregar_producto, mostrar_inventario, procesar_venta, inventario
while True:
  print("Menu Comercio ALMA ZEN")
  print("1. Agregar producto")
  print("2. Mostrar inventario")
  print("3. Procesar Venta")
  print("4. Generar informe")
  print("5. Salir")
 opcion=input("Ingrese una opción: (1-5)") 
  if opcion == "1":
    agregar_producto()
  elif opcion == "2":
    mostrar_inventario()
  elif opcion == "3":
     procesar_venta()
  elif  opcion == "4":
    generar_informe()
  elif opcion == "5":
        print("Saliendo del programa...")
        break
  else:
        print("Opción inválida.")
      
