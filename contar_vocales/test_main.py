from contar_vocales.main import contar_vocales
def test_string_vacio_no_tiene_vocales():
    assert(contar_vocales("") == 0)


