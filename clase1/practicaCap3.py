
def det_mayor(arreglo):
    mayor=0
    for i in range(len(arreglo)):
        if arreglo[i]>mayor:
            mayor=arreglo[i]
    return mayor


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
        dato=int(input())
        arreglo[i]=dato

def registrarWhile(arreglo, msj):
    i=0
    while i<len(arreglo, msj):
        print(f" {msj} a guardar en la posiscion {i+1}")
        dato=input()
        arreglo[i]=dato
        i=i+1


nombres=[""]*5
estados=["","","","","","",""]
precios=[0]*7


cargar(precios, "Ingresa el precio")
mostrar(precios)
print()
precioMayor=det_mayor(precios)
print(f"El precio mayor es {precioMayor}")