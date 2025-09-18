from FizzBuzz import fizzbuzz


def test_fizz_buzz_three():
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(3) == "FizzFizz"

def test_fizz_buzz_five():
    assert fizzbuzz(5) == "BuzzBuzz"

def test_fizz_buzz_other_number():
    assert fizzbuzz(4) == "4"

def test_fizz_buzz_both_three_five():
    assert fizzbuzz(15) == "BuzzFizzBuzz"
    assert fizzbuzz(30) == "FizzFizzBuzz"

def test_fizz_buzz_13():
    assert fizzbuzz(13) == "Fizz"