from reversa.main import reversa

def test_devuelve_misma_entrada_si_el_string_es_vacio():
    assert(reversa("") == "")

def test_devuelve_misma_entrada_si_string_es_longitud_uno():
    assert(reversa("a") == "a")

def test_devuelve_reversa_entrada_si_string_es_longitud_dos():
    assert(reversa("ab") == "ba")

