#Usuario
nombre_usuario= "alma"
contraseña="2794"

def iniciar_sesion():
   intentos=3
    while intentos > 0:
        usuario_ingresado = input("Nombre de usuario: ")
        contraseña_ingresada = input("Contraseña: ")
        if usuario_ingresado == nombre_usuario and contraseña_ingresada == contraseña:
            print("Inicio de sesión exitoso. ¡Bienvenido")
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")
            intentos -= 1
    print("Número de intentos agotados. Por favor, inténtelo más tarde.")
    return False
if iniciar_sesion():
    #Aca empieza a correr lo que lleva el menu
    inventario =[]
    def agregar_producto():
       codigo = int(input("Ingrese el codigo del producto:  "))
       nombre = input("Ingrese el nombre del producto:   ")
       cantidad = int(input("Ingrese la cantidad del producto: "))
       precio = float(input("Ingrese el precio del producto: "))
       inventario.append([codigo, nombre, cantidad, precio])
       print(f"Producto '{nombre}' agregado al inventario.")
        
    def mostrar_inventario():
        if inventario:
           print("Inventario:  ")
           for producto in inventario:
               codigo, nombre, cantidad, precio_unitario = producto
               total_valor = cantidad * precio_unitario
               print(f"Codigo: {codigo}, Nombre: {nombre}, Cantidad: {cantidad}, Precio unitario: ${precio_unitario:.2f}, Total valor: ${total_valor:.2f}")
        else:
            print("El inventario esta vacio")

    def procesar_venta():

       nombre=input("Ingrese el nombre del producto a vender:")
       cantidad= int(input("Ingrese la cantidad a vender:"))
       for producto in inventario:
          if producto[1] == nombre:
            if producto[2]>= cantidad:
                producto[2] -= cantidad
                print("----Boleta----")
                print(f"Venta procesada: Se vendieron {cantidad} unidades de '{nombre}'.")
                precio_sin_iva= producto[2]*cantidad
                precio_sin_iva= precio_sin_iva*1.19 #impuesto de iva
                print(f"Venta procesada: Se vendio {cantidad} unidades de '{nombre}' por un total de ${precio_con_iva:.2f} (IVA 19% incluido).")
             else:
                print(f"No hay suficientes unidades de '{nombre}' en stock.")
            break
        else:
           print(f"El producto '{nombre}' no está en el inventario.")

def generar_informe():
   if inventario:
      total_productos= len(inventario)
      total_cantidad=sum (producto[2] for producto in inventario)
      total_valor= sum(producto[2]* producto[3] for producto in inventario)
      print("Informe del inventario:")
      print (f"Total de productos: {total_productos}")
      print (f"Total de unidades en stock: {total_cantidad}")
      print (f"Valor total del inventario: ${total_valor:.2f}")
    else:
       print ("El inventario está vacío.")
       



                
                                                                                                       
                
                
           
            
     
    
    
    
    
    
    

           

  
            
            
        
                
        
                    
                    
                    
                    
        
              
