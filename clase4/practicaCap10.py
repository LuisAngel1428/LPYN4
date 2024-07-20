def cargar(arreglo, arreglo2, arreglo3):
    while True:
        dato=input("Ingrese el nombre: ")
        dato2=validarPositivo("Ingrese la edad ")
        dato3=validarPositivo("Entradas al cine ")
        arreglo.append(dato)
        arreglo2.append(dato2)
        arreglo3.append(dato3)
        resp=input("Presione espacio para detener. ")
        if resp==" ":
            break

def menu_opciones():
    print("""
1--> Registrar
2--> Imprimir
3--> Salir
Ingrese la opción""")
    
def mostrar(arreglo, arreglo2, arreglo3):
    print("--------------------------")
    print("Datos cargados")
    print("--------------------------")
    for i in range(len(arreglo)):
        print(f"{arreglo[i]} Edad: {arreglo2[i]} Cantidad: {arreglo3[i]}")

def validarPositivo(mensaje):
    num=-1
    while not (num>0):
        print(mensaje)
        num=int(input())
        if not (num>0):
            print("Debe ser positivo.")
        else:
            return num
        
#cuerpo principal

nombres=[]
edades=[]
Cantidades=[]
while True:
    menu_opciones()
    opcion=int(input())
    match opcion:
        case 1:
            cargar(nombres, edades, Cantidades)
        case 2:
            mostrar(nombres, edades, Cantidades)
        case 3:
            print("Hasta luego")
        case _:
            print("Opción errada")
    if opcion==3:
        break