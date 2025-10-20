from factores_primos.main import factores_primos

def numeros_menores_a_dos_no_tienen_factor_primo():
    assert(factores_primos(0) == [])
    assert(factores_primos(1) == [])
