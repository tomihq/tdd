from contar_vocales.main import contar_vocales
def test_string_vacio_no_tiene_vocales():
    assert(contar_vocales("") == 0)

def test_string_tiene_una_vocal():
    assert(contar_vocales("a") == 1)

def test_string_tiene_una_consonante():
    assert(contar_vocales("b") == 0)
