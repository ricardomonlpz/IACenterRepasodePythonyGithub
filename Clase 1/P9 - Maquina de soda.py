#Máquina de sodas
costo_soda=17
saldo=0

while saldo <costo_soda:
    #Mostrar monto adeudado
    print("Restan",costo_soda-saldo)
    
    #Solicitar ingresar moneda
    valor_moneda=int(input("Ingresa una modenda: "))

    #Verificación de moneda
    
    if valor_moneda == 1 or valor_moneda == 2 or valor_moneda == 5 or valor_moneda == 10:
        saldo=saldo+valor_moneda
    else:
        print("La moneda no es aceptada")
    
print("Toma tu soda, tu cambio es:",saldo-costo_soda)

