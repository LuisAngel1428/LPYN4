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

diasSemana=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
estadosVenezuela=["Amazonas", "Apure","Carabobo","Cojedes","Falcon", "Lara", "Merida", "Miranda", "Monagas", "Portuguesa"]
mesesAño=["Enero","Febrero","Marzo","Abril","Mayo", "Junio","Julio","Agosto", "Septiembre", "Octubre","Noviembre","Diciembre"]
valoresDolar=[36.40, 39.40, 41.00, 40.10, 36.80]

#completar