from fizzbuzz.main import fizzbuzz


def test_fizzbuzz_imprime_mismo_numero_si_no_es_divisible_ni_por_3_ni_5():
    assert(fizzbuzz(2) == "2")

def test_fizzbuzz_imprime_fizz_si_es_divisible_por_3():
    assert(fizzbuzz(3) == "fizz")

def test_fizzbuzz_imprime_buzz_si_es_divisible_por_5():
    assert(fizzbuzz(5) == "buzz")

def test_fizzbuzz_imprime_fizz_buzz_si_es_divisible_por_3_y_5():
    assert(fizzbuzz(15) == "fizzbuzz")

