# Comercio_libreria.py

# Usuario
nombre_usuario = "alma"
contraseña = "2794"

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

def agregar_producto():
    while True:
        try:
            codigo = int(input("Ingrese el código del producto: "))
            break
        except ValueError:
            print ("Error: El código debe ser un número entero. Por favor, inténtelo de nuevo.")
    nombre = input("Ingrese el nombre del producto: ")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Error: La cantidad debe ser un número entero. Por favor, inténtelo de nuevo.")
    precio = float(input("Ingrese el precio del producto: "))
    inventario.append([codigo, nombre, cantidad, precio])
    print(f"Producto '{nombre}' agregado al inventario.")

def mostrar_inventario():
    if inventario:
        print("Inventario:")
        for producto in inventario:
            codigo, nombre, cantidad, precio_unitario = producto
            total_valor = cantidad * precio_unitario
            print(f"Código: {codigo}, Nombre: {nombre}, Cantidad: {cantidad}, Precio unitario: ${precio_unitario:.2f}, Total valor: ${total_valor:.2f}")
    else:
        print("El inventario está vacío.")

def procesar_venta():
    nombre = input("Ingrese el nombre del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    for producto in inventario:
        if producto[1] == nombre:
            if producto[2] >= cantidad:
                producto[2] -= cantidad
                precio_sin_iva = producto[3] * cantidad
                precio_con_iva = precio_sin_iva * 1.19  # impuesto de IVA
                print("----Boleta----")
                print(f"Venta procesada: Se vendieron {cantidad} unidades de '{nombre}'.")
                print(f"Venta procesada: Se vendieron {cantidad} unidades de '{nombre}' por un total de ${precio_con_iva:.2f} (IVA 19% incluido).")
                return
            else:
                print(f"No hay suficientes unidades de '{nombre}' en stock.")
                return
    print(f"El producto '{nombre}' no está en el inventario.")

                
                                                                                                       
                
                
           
            
     
    
    
    
    
    
    

           

  
            
            
        
                
        
                    
                    
                    
                    
        
              
