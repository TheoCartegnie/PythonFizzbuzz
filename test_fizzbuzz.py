from FizzBuzz import fizzbuzz


def test_fizz_buzz_three():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_fizz_buzz_five():
    assert fizzbuzz(5) == "Buzz"

def test_fizz_buzz_other_number():
    assert fizzbuzz(4) == 4

def test_fizz_buzz_both_three_five():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def test_fizz_buzz_13():
    assert fizzbuzz(13) == "Fizz"