from factores_primos.main import factores_primos

def test_numeros_menores_a_dos_no_tienen_factores_primos():
    assert(factores_primos(0) == [])
    assert(factores_primos(1) == [])

def test_numero_2_esta_incluido_en_sus_factores_primos():
    assert(factores_primos(2) == [2])

def test_numero_3_esta_incluido_en_sus_factores_primos():
    assert(factores_primos(3) == [3])

def test_numero_4_su_factor_primo_es_2_y_un_primo():
    assert(factores_primos(4) == [2, 2])

def test_numero_6_es_producto_de_dos_primos():
    assert(factores_primos(6) == [2, 3])
