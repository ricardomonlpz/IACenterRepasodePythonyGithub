
#Declaracion de listas
Usuarios=[]
Contraseñas=[]
x=True

while x==True:
    Crear_Usuario=input("¿Desea crerar un nuevo usuario? (s:sí , n:no) ")
    if Crear_Usuario=="s":
        Nombre_Usuario=input("Ingrese el nombre de usuario: ")
        if Nombre_Usuario in Usuarios:
            Cambiar_contraseña=input("El usuario ya existe, ¿desea cambiar la contraseña? (s:sí , n:no) ")
            if Cambiar_contraseña=="s":
                    indice = Usuarios.index(Nombre_Usuario)
                    Contraseñas[indice]= input("Ingrese la nueva contraseña: ")
            else:
                print("No se a generado ningun cambio")
        else:
            Usuarios.append(Nombre_Usuario)
            Contraseña=input("Ingresa la contrasaseña del usuario: ")
            Contraseñas.append(Contraseña)
    else:
        x=False
print(F"\tUsuarios\tContraseñas")
for i in range :
    print(F"\t{Usuarios(i)}\t{Contraseñas(i)}")