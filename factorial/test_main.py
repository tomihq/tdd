from factorial.main import factorial

def test_arroja_error_si_es_negativo():
    assert(factorial(-1) == "number must be positive")

def test_factorial_0_es_1():
    assert(factorial(0) == 1)

def test_factorial_1_es_1():
    assert(factorial(1) == 1)

def test_factorial_2_es_2():
    assert(factorial(2) == 2)
