#Declaración de lista
lista = [1,2,3,4,5]
print(lista)

#Sustitución de elemento del centro
cambio = int(input("Intruduce un valor para el centro de la lista: "))
lista[2]=cambio
print(lista)

#Eliminación de ultimo elemento
lista.pop(-1)
print(lista)

print(len(lista))