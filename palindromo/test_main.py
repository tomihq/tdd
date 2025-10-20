from palindromo.main import palindromo

def test_devuelve_la_entrada_si_el_string_es_vacio():
    assert(palindromo("") == "")

def test_devuelve_misma_entrada_si_string_es_longitud_uno():
    assert(palindromo("a") == "a")
