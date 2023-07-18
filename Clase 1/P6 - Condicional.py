#Solucitud de ingreso de numero
num = int(input('Ingresa un numero:'))

#Obtención de modulo y compración de par e impar
if num%2 == 0:
    print(num,"es un numero par")
elif num%2 == 1:
    print(num,"es un numero impar")