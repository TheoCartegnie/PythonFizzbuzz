def fizzbuzz(a):
    word = ""
    if a % 3 == 0 or a % 5 == 0:
        if a % 3 == 0 and a % 5 == 0:
             word += "FizzBuzz"
        if a % 5 == 0 :
             word += "Buzz"
        elif a % 3 == 0:
             word += "Fizz"
        a = str(a)
        for char in a:
            if a == "3":
                word += "Fizz"
            if a == "5":
                word += "Buzz"
    return word

def fizzbuzz_main():
    for a in range(1, 101):
        print(fizzbuzz(a))

if __name__ == "__main__":
    pass