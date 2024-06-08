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
           
            
     
    
    
    
    
    
    

           

  
            
            
        
                
        
                    
                    
                    
                    
        
              
