from FizzBuzz import fizzbuzz


def test_fizz_buzz_three():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_fizz_buzz_five():
    assert fizzbuzz(5) == "Buzz"

def test_fizz_buzz_other_number():
    assert fizzbuzz(4) == 4