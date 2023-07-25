numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
numero4 = int(input("Ingresa el cuarto número: "))

if numero1 >= numero2 and numero1 >= numero3 and numero1 >= numero4:
    print("El numero",numero1,"es el numero mas grande")
elif numero2 >= numero1 and numero2 >= numero3 and numero2 >= numero4:
    print("El numero",numero2,"es el numero mas grande")
elif numero3 >= numero1 and numero3 >= numero2 and numero3 >= numero4:
    print("El numero",numero3,"es el numero mas grande")
else:
    print("El numero",numero4,"es el numero mas grande")