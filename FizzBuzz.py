def fizzbuzz(a):
    word = ""
    b = str(a)

    for char in b:
        if char == "3":
            word += "Fizz"
        if char == "5":
            word += "Buzz"

    if a % 3 == 0:
         word += "Fizz"
    if a % 5 == 0 :
         word += "Buzz"


    if len(word) == 0:
        return b
    return word

def fizzbuzz_main():
    for a in range(1, 101):

        print("Index : ", a, " resultat => ",fizzbuzz(a))

if __name__ == "__main__":
    fizzbuzz_main()