from lib.fizzbuzz import *

def test_fizzbuzz_when_passing_in_3_returns_fizz():
    actual = fizzbuzz(3)
    expected = 'Fizz'

    assert actual == expected