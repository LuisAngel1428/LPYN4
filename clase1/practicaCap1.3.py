nombres=["Maria","Fabiana","Paola", "Vanesa", "Nathaly", "Raulymar"]

print(nombres)
posicion=int(input("Ingresa la posición que deseas conocer: "))
if posicion>=0 and posicion<=len(nombres):
    print(nombres[posicion-1])
else:
    print(f"El indice fuera de rango, las posiciones van desde 1 a {len(nombres)}")