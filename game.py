secuencia_texto = input("Ingrese la secuencia de numeros: ")
secuencia = []
for items in secuencia_texto.split(','):
    secuencia.append(int(items))

def tableroVacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def contenidoColumna(numColumna, tablero):
    columna = []
    for fila in tablero:
        celda = fila[numColumna - 1]
        columna.append(celda)
    return columna

def contenidoFila(numFila, tablero):
    fila = []
    for columna in tablero:
        celda = columna[numFila - 1]
        fila.append(celda)
    return fila

def allColumnas(tablero):
    allColumna = []
    for i in range(1, 8):
        allColumna.append(contenidoColumna(i, tablero))
    return allColumna

def allFilas(tablero):
    return tablero

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range (6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return

def completarTableroEnOrden(secuencia, tablero):
    for turno in range(len(secuencia)):
        if turno%2 == 0:
            soltarFichaEnColumna(1, secuencia[turno], tablero)
        else:
            soltarFichaEnColumna(2, secuencia[turno], tablero)
    return tablero

def dibujarTablero(tablero):
    for fila in tablero:
        print("|", end="")
        for celda in fila:
            if celda == 0:
                print("   ", end="")
            else:
                print("%s " %celda, end=" ")
        print("|")
    for i in range(0, 23):
        if i == 0 or i == 22:
            print("+", end="")
        else:
            print("-", end="")
    print("\n")

def validSequence(secuencia):
    for se in secuencia:
        if se < 1 or se > 7:
            return False
    else:
        return True

tablero = []
if  validSequence(secuencia):
    tablero = completarTableroEnOrden(secuencia, tableroVacio())
    dibujarTablero(tablero)
else:
    print("La sequencia es invalida")

print(contenidoColumna(2, tablero))
print(contenidoFila(1, tablero))
print(allColumnas(tablero))
print(allFilas(tablero))
