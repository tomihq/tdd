from fizzbuzz.main import fizzbuzz

def test_fizzbuzz_imprime_fizz_si_es_divisible_por_3():
    assert(fizzbuzz(3) == "fizz")


def test_fizzbuzz_imprime_buzz_si_es_divisible_por_5():
    assert(fizzbuzz(5) == "buzz")

