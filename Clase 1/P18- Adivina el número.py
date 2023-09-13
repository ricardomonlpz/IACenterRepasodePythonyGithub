#importar modulo(s) necesarios
import random

#Definir una funciaón para introducir un número entero

def obtener_numero_usuario():
    print("Bienvenido a Adivina el número")
    while True:
        try:
            numero = int(input("Introduce tu intento (entre 1 y 100): "))
            if 1 <= numero <= 100:
                return numero
            else:
                print("Por favor, ingresa un número entre 1 y 100.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

print("Estoy pensando en un número entero entre 0 y 100")
print("Crees poder adivinarlo?")


def obtener_numero_aleatorio():
    return random.randint(1, 100)

# Número de intentos
intentos = 5


#Avisa al usuario cuantos intentos le quedan
numero_objetivo = obtener_numero_aleatorio()
print(f"Bienvenido al juego de adivinanza. Tienes {intentos} intentos para adivinar el número secreto.")

for intento_actual in range(1, intentos + 1):
    print(f"Intento {intento_actual}:")
    #Solicitar numero
    numero_usuario = obtener_numero_usuario()

    #Verificar si se adivino el número y actuar en consecuencia
    if numero_usuario == numero_objetivo:
        #Mostar mensaje de falicidades si se adivinó en numero
        print("¡Felicitaciones! Has adivinado el número correcto.")
        break
    #Verificar si el numero introducido es menor al buscado, si es asi dar pista
    elif numero_usuario < numero_objetivo:
        print("El número es mayor.")
    #Verificar si el numero introducido es mayor al buscado, si es asi dar pista
    else:
        print("El número es menor.")
else:
    #Mostar mensaje de juego terminado y cuál era el numero a adivinar
    print(f"Se acabaron los intentos. El número correcto era {numero_objetivo}.")