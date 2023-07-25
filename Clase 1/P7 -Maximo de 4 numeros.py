numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
numero4 = int(input("Ingresa el cuarto número: "))

if numero1 >= numero2:
    nummax=numero1
else:
    nummax=numero2

if numero3 >= nummax:
    nummax=numero3

if numero4 >= nummax:
    nummax=numero4

print("El numero más grande es:",nummax)