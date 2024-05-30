# Inicializar una matriz vacía para almacenar productos (inventario)
inventario = []

# identifica usuario
usuario = []
while True:
    usuario = input("Ingrese su nombre de usuario:")
    contrasena = input("Ingrese su contraseña:")
    break
#Comienza el menu del comercio
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
    elif opcion =="3":
        nombre = input("Ingrese el nombre del producto a vender:  ")
        cantidad = int(input("Ingrese la cantidad a vender:  "))
        for producto in inventario:
            if producto[0] == nombre:
                if producto[1] >= cantidad:
                    producto[1] -= cantidad
                    precio_sin_iva = producto[2] * cantidad
                    precio_con_iva = precio_sin_iva * 1.19   #Impuesto de iva 19%
                    print(f"Venta procesada: Se vendio {cantidad} unidades de '{nombre}' por un total de ${precio_con_iva:.2f} (IVA 19% incluido).")
                else:
                    print(f"No hay suficiente unidades de '{nombre}' en stock.")
        else:
            print(f"El producto '(nombre)'no esta en el inventario.")
elif opcion == "4":
     if inventario:
        total_productos = len(inventario)
        total_cantidad = sum(producto[1] for producto in inventario)
        total_valor = sum(producto[1] * producto[2] for producto in inventario)
        print("Informe del inventario:")
        print(f"Total de productos: {total_productos}")
        print(f"Total de unidades en stock: {total_cantidad}")
        print(f"Valor total del inventario: ${total_valor:.2f}")
     else:
        print("El inventario esta vacio.")
elif opcion == "5":
    print("Saliendo del programa...")
    break
else:
    print("Opcion Invalida.")

  
            
            
        
                
        
                    
                    
                    
                    
        
              
