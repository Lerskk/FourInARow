from src.game import validSequence

def test_valid_sequence():
    secuencia = [1, 2, 3]

    assert validSequence(secuencia) == True