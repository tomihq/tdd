from factores_primos.main import factores_primos

def test_numeros_menores_a_dos_no_tienen_factores_primos():
    assert(factores_primos(0) == [])
    assert(factores_primos(1) == [])

def test_numero_2_esta_incluido_en_sus_factores_primos():
    assert(factores_primos(2) == [2])

def test_numero_3_esta_incluido_en_sus_factores_primos():
    assert(factores_primos(3) == [3])
