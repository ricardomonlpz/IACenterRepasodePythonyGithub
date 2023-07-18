#Ingresa los datos correspondientes a la hora inicial

inicial_hora=int(input("Ingresa la hora incial: "))
inicial_minutos=int(input("Ingresa los minutos de la hora inicial: "))
duracion=int(input("Ingresa el tiempo que duro la actividad en minutos: "))

#Calcula la hora final

minutos=inicial_minutos+duracion

final_hora=inicial_hora+(minutos//59)
final_minutos=minutos-(60*(minutos//59))

print("La hora final de la tarea es: ",final_hora,":",final_minutos,sep="")