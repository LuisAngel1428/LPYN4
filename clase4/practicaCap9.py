def cargar(arreglo):
    while True:
        dato=input("Ingrese el dato: ")
        arreglo.append(dato)
        resp=input("Presione espacio para detener. ")
        if resp==" ":
            break

def menu_opciones():
    print("""
1--> Registrar
2--> Imprimir
3--> Salir
Ingrese la opción""")
    
def mostrar(arreglo):
    print("--------------------------")
    print("Datos cargados")
    print("--------------------------")
    for i in range(len(arreglo)):
        print(arreglo[i])

#cuerpo principal

nombres=[]
while True:
    menu_opciones()
    opcion=int(input())
    match opcion:
        case 1:
            cargar(nombres)
        case 2:
            mostrar(nombres)
        case 3:
            print("Hasta luego")
        case _:
            print("Opción errada")
    if opcion==3:
        break