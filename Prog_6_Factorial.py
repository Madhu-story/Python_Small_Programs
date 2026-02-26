# Find the Factorial of the given number:
print()
def factorial(num):
    fact = 1
    if num == 0 or num == 1:
        num = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

result = factorial(5)
print("Factorial:", result)

print()
# Find the Factorial of the given number using recursion:
print("------------Factorial using recursion---------------")
print()

# def fact(num):
#     res = 1
#     for i in range(1, num+1):
#         if i <= num:
#             res *= i
#             fact(num-1)
#     return res

# result = fact(5)
# print("Factorial using recursion:", result)

def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)

result = fact(5)
print("Factorial using recursion:", result)