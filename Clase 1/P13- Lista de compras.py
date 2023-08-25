Productos=[]
Cantidades=[]
x=True
while x == True:
    pregunta=input("Desea agragar un producto a la lista: c:continuar, s:salir ")
    if pregunta=="c":
        x=True
        producto=input("Ingresa el nombre del producto: ")
        Productos.append(producto)
        Cantidad= input("Ingresa el numero de elementos: ")
        Cantidades.append(Cantidad)
    else:
        x=False

print ("\n\tProducto \tcantidades")
for n in range(len(Productos)):
    print (f"\t{Productos[n]} \t    {Cantidades[n]}")