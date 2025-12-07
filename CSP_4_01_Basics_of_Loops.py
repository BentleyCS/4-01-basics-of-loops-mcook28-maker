#All questions must use a loop for full points.
import random

def oddNumbers(n: int) -> str:
    result = ""                     # ← MUST be indented INSIDE the function

    for i in range(1, n + 1):       # loop starts here
        if i % 2 != 0:              # check odd
            result += str(i) + " "  # add to result

    return result.strip()           # return final string
def backwards(n)-> str:
    if n < 1:
        return ""
    result = ""
    for i in range(n, 0, -1):
        result += str(i) + " "
    return result.strip()
def randomRepeating():
    tries = 0
    while True:
        roll = random.randint(1, 10)
        tries += 1
        if roll == 10:
            break
    print(f"it took {tries} tries to get a 10")
def randomRange(n):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(1, 100))
    print(f"Highest number: {max(numbers)}, Lowest number: {min(numbers)}")
def reverse(word:str)->str:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word
def fizzBuzzContinuous(n):
    result = ""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result += "fizzbuzz "
        elif i % 3 == 0:
            result += "fizz "
        elif i % 5 == 0:
            result += "buzz "
        else:
            result += str(i) + " "
    return result.strip()
def collatz(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    print(1)
def fibonacci(n):
    if n <= 0:
        return ""
    fib_seq = []
    a, b = 0, 1
    for i in range(n):
        fib_seq.append(str(a))
        a, b = b, a + b
    return " ".join(fib_seq)
print(backwards(5))
print(reverse("Hello"))
print(fizzBuzzContinuous(15))
print(fibonacci(10))
collatz(6)
randomRepeating()
randomRange(5)