from reversa.main import reversa

def test_devuelve_misma_entrada_si_el_string_es_vacio():
    assert(reversa("") == "")

def test_devuelve_misma_entrada_si_string_es_longitud_uno():
    assert(reversa("a") == "a")

def test_devuelve_reversa_entrada_si_string_es_longitud_dos():
    assert(reversa("ab") == "ba")

def test_devuelve_reversa_entrada_si_string_es_longitud_tres():
    assert(reversa("abc") == "cba")

def test_devuelve_reversa_entrada_si_string_es_longitud_n():
    assert(reversa("+ab!cde_f98gh143") == "341hg89f_edc!ba+")
