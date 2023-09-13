registro_temperatura = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

for i in range(5):
    for j in range(4):
        registro_temperatura[i][j]=float(input("Ingresa la temperatura"))

for x in registro_temperatura:
    print (x)

tem_promedio=0
for index in range(len(registro_temperatura)):
    tem_promedio+=registro_temperatura[index][2]

tem_promedio_medio=tem_promedio/5

print("El promedio de temperatura al medio dia es:", tem_promedio_medio)

for fila in registro_temperatura:
    for elemento in fila:
        if elemento > maximo:
            maximo = elemento


print("La temperatura maxima es:", maximo)