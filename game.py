secuencia = [1, 2, 3, 1, 8]
def tableroVacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

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
        for celda in fila:
            if celda == 0:
                print(" ", end="")
            else:
                print("%s" %celda, end=" ")
        print("")

def validSequence(secuencia):
    for se in secuencia:
        if se < 1 or se > 7:
            return False
    else:
        return True

if  validSequence(secuencia):
    dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio() ) )
else:
    print("La sequencia es invalida")