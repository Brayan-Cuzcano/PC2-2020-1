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


# Pregunta numero 3

def mueve_col():
    import Numpy as np
    b=np.array([(34,43,73,25,10),(82,22,12,14,10),(53,94,66,84,10),(35,73,24,34,10)])
    print(b)