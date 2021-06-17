from src.game import contenidoColumna

def test_contenido_columna():
    tablero = [
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0],
    ]
    sum = 0

    for celda in contenidoColumna(3, tablero):
        sum += celda

    assert sum == 9