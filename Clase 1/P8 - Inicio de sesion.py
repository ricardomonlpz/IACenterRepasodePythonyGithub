#Valores correctos de las contraseñas

usuario_correcto="Usuario1"
contrasena_correnta="password123"

#Solicitud de usuario

usuario=input("Ingresa tu usuario: ")
contrasena=input("Ingresa tu contraseña: ")

#Verificación de usuario
if usuario == usuario_correcto:
    if contrasena == contrasena_correnta:
        print("Bienvenido")
    else:
        print("La contraseña introducida no es correcta")
else:
    print("El usuario introducido no está registrado")
