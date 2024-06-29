def imprimir_for(arreglo):#ciclo for each
    for value in arreglo:
        print (value)

def imprimir_for_i(arreglo):#ciclo for usando el indice
    for i in range(len(arreglo)):
        print(arreglo[i])

def mostrar(arreglo):
    i=0
    while i<len(arreglo):
        print(arreglo[i])
        i=i+1

def cargar(arreglo, msj):
    for i in range(len(arreglo)):
        print(f" {msj} a guardar en la posiscion {i+1}")
        dato=input()
        arreglo[i]=dato

def registrarWhile(arreglo, msj):
    i=0
    while i<len(arreglo):
        print(f" {msj} a guardar en la posiscion {i+1}")
        dato=input()
        arreglo[i]=dato
        i=i+1

#cuerpo principal

nombres=[""]*5
estados=["","","","","","",""]

print(nombres)
print(estados)
print("Nombres")
cargar(nombres, "Ingresa el nombre")
print("Estados de Venezuela")
registrarWhile(estados, "Nombre del estado")
mostrar(nombres)
print("Estados de Venezuela")
imprimir_for_i(estados)

