from factorial.main import factorial

def test_arroja_error_si_es_negativo():
    assert(factorial(-1) == "number must be positive")

def test_factorial_0_es_1():
    assert(factorial(0) == 1)
