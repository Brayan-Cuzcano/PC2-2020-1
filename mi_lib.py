# Pregunta numero 2
from random import randint
m=int(input("Ingrese el numero de filas: "))
n=int(input("Ingrese el numero de columnas: "))
def crea_arreglo (m,n):
    M=[]
    for i in range (m):
        M.append([]*n)

    for i in range (m):
        for j in range (n):
            M[i].append(randint(0,100))

    cadena=""
    for i in range(m):
        for j in range(n):
            cadena=cadena+"\t"+str(M[i][j])
        cadena=cadena+"\n"
    return cadena
print(str(crea_arreglo(m,n)))
