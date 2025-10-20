from factorial.main import factorial

def test_arroja_error_si_es_negativo():
    assert(factorial(-1) == "number must be positive")
