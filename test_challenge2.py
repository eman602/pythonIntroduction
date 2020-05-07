import Hard_primeNumbers
import challenge2


def test_here():
    result = challenge2.factorial(8)
    assert result==40320

def test_primenumbers():
    result = Hard_primeNumbers.primeNumbers(8)
    assert result =={2, 3, 5, 7}