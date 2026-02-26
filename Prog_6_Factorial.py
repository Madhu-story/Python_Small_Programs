# Find the Factorial of the given number:


def factorial(num):
    fact = 1
    if num == 0 or num == 1:
        num = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

result = factorial(5)
print("Factorial: ", result)