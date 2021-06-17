from src.game import contenidoFila

def test_contenido_fila():
    tablero = [
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0],
    ]
    sum = 0

    for celda in contenidoFila(6, tablero):
        sum += celda

    assert sum == 3
